import numpy as np
N = int(input())
F = np.array([list(map(int, input().split())) for i in range(N)])
P = np.array([list(map(int, input().split())) for i in range(N)])
ans = -10**18
for i in range(2**10):
    box = []
    for k in range(10):
        if ((i>>k)&1):
            box = [1]+ box
        else:
            box = [0]+ box
    if all(i == 0 for i in box):
        continue
    # box は開業する0~9の候補リスト
    # G は F(0か1の各店開業状況)
    G = np.sum(F*box, axis=1)
    a = 0
    for x,y in zip(G,P):
        a += y[x]
    ans = max(ans, a)
    
print(ans)
