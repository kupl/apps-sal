(n, m) = map(int, input().split())
stu = []
che = []
kyori = []
ans = []
for _ in range(n):
    stu.append(list(map(int, input().split())))
for _ in range(m):
    che.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        kyori.append(abs(stu[x][0] - che[y][0]) + abs(stu[x][1] - che[y][1]))
    z = min(kyori)
    ans.append(kyori.index(z) + 1)
    kyori = []
for i in range(len(ans)):
    print(ans[i])
