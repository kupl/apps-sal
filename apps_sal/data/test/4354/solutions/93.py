n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for j in range(m)]

for i in range(n):
    l = []
    for j in range(m):
        dist = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        l.append(dist)
    goal = l.index(min(l)) + 1
    print(goal)
