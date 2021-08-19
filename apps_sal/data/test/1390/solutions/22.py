(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
res = 10 ** 100
for i in range(m - n + 1):
    res = min(res, A[n + i - 1] - A[i])
print(res)
