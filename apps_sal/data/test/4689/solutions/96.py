k, n = map(int, input().split())
A = list(map(int, input().split()))
d = 0

for i in range(n - 1):
    d = max(d, A[i + 1] - A[i])

d1 = (k - A[n - 1]) + A[0]
d = max(d, d1)
print(k - d)
