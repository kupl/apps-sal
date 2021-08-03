n = int(input())

S = list(map(int, input().split()))
K = [0] * 9
m = min(S)
d = 0
di = 0
len = n // m
if not len:
    print(-1)
else:
    for i in range(8, -1, -1):
        if S[i] == m:
            d = i + 1
            break
    n -= (n // m) * m
    S = list(map(lambda x: x - m, S))
    for i in range(8, -1, -1):
        if S[i]:
            print(str(i + 1) * (n // S[i]), end='')
            len -= n // S[i]
            n -= (n // S[i]) * S[i]
        else:
            print(str(i + 1) * len)
            n = 0
            break
