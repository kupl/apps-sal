n, k = map(int, input().split())

m, M = 0, 0

if n > k > 0:
    m = 1

K = (n + 2) // 3
if k < K:
    M = k * 2
else:
    M = n - k

print(m, M)
