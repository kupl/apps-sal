(n, m) = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]
road = sum(road, [])
for i in range(1, n + 1):
    print(road.count(i))
