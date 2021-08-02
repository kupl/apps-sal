n, m = map(int, input().split())
road_list = []

for _ in range(m):
    a, b = (input().split())
    road_list.append(a)
    road_list.append(b)

for i in range(1, n + 1):
    print(road_list.count(str(i)))
