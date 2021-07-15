import numpy as np
H, W = map(int, input().split())
S = []
pad = list('.'* (W+2))
S.append(pad)
for i in range(H):
    _S = list(input())
    _S = ['.'] + _S +[ '.']
    S.append(_S)
S.append(pad)
S = np.array(S)

for h in range(1, H+1):
    for w in range(1, W+1):
        if S[h, w] == '#':
            print('#', end='')
        else:
            print(np.sum(S[h-1:h+2, w-1:w+2]=='#'), end="")
    print()

        
