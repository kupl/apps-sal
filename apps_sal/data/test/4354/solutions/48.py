n, m = map(int, input().split())

s = [tuple(map(int, input().split())) for _ in range(n)]
c = [tuple(map(int, input().split())) for _ in range(m)]

for a, b in s:
    d = float('inf')
    for i in range(m):
        x, y = c[i]
        if abs(a - x) + abs(b - y) < d:
            d = abs(a - x) + abs(b - y)
            ans = i + 1
    print(ans)
