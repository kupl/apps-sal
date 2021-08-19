(N, M) = list(map(int, input().split()))
stu = []
che = []
for i in range(N):
    ab = list(map(int, input().split()))
    stu.append(ab)
for i in range(M):
    cd = list(map(int, input().split()))
    che.append(cd)
ans = 0
dis = 0
x = 5 * 10 ** 8
for i in range(N):
    for j in range(M):
        dis = abs(stu[i][0] - che[j][0]) + abs(stu[i][1] - che[j][1])
        if dis < x:
            x = dis
            ans = j + 1
    print(ans)
    x = 5 * 10 ** 8
