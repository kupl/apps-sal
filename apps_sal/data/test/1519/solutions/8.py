(n, m, a) = map(int, input().split())
l = [[*map(int, input().split())] for _ in range(n)]
prev = 0
res = 0
for (x, y) in l:
    res += (x - prev) // a
    prev = x + y
res += (m - prev) // a
print(res)
