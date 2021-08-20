N = int(input())
S = input()
if N % 2 == 0:
    T = S[0:int(N / 2)]
    if T + T == S:
        print('Yes')
    else:
        print('No')
else:
    print('No')
