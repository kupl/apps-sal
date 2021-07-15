N, M = list(map(int, input().split()))
if N > M:
    N, M = M, N
res = 0
if N == 1 and M == 1:
    res = 1
elif N == 2:
    res = 0
else:
    res = max(1, N - 2) * max(1, M - 2)
print(res)

