m, n, k = list(map(int, input().split()))
s = 0
for i in range(k):
    s += 2 * m
    s += 2 * n - 4
    m -= 4
    n -= 4
print(s)
