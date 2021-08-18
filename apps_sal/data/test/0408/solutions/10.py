n, m = list(map(int, input().split()))
c = min(n, m // 2)
res = 0
for i in range(c + 1):
    n1 = n - i
    m1 = m - i * 2
    res = max(res, i + min(n1 // 2, m1))
print(res)
