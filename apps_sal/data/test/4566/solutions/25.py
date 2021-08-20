(n, m) = map(int, input().split())
roads = [0 for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    roads[a - 1] += 1
    roads[b - 1] += 1
for i in roads:
    print(i)
