N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


N -= K
res = 1
if N > 0:
    res += (N + (K - 1) - 1) // (K - 1)
print(res)
