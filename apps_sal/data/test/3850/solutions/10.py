n, k, p = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
a.sort()
b.sort()

res = 2147483647
for i in range(k - n + 1):
    m = 0
    for j in range(n):
        k = j + i
        dis = abs(a[j] - b[k]) + abs(b[k] - p)
        m = max(m, dis)
    res = min(res, m)
print(res)
