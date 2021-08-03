n, S = map(int, input().split())
a = list(map(int, input().split()))
l, r, m, cost = 0, n + 1, -1, -1
while r - l > 1:
    m = (l + r) // 2
    cost = sum(sorted([a[i] + (i + 1) * m for i in range(n)])[:m])
    l, r = ((l, m) if cost > S else (m, r))
print(l, sum(sorted([a[i] + (i + 1) * l for i in range(n)])[:l]))
