N, M = map(int, input().split())
stu = [0] * N
for i in range(N):
    stu[i] = list(map(int, input().split()))

cp = [0] * M
for i in range(M):
    cp[i] = list(map(int, input().split()))

# print(stu,cp)
stumo = [0] * N
for i in range(N):
    min_move = 10000000000000000000000000
    for j in range(M):
        min_his = min_move
        mhd = abs(stu[i][0] - cp[j][0]) + abs(stu[i][1] - cp[j][1])
        min_move = min(min_move, mhd)
        if(min_move != min_his):
            stumo[i] = j + 1
# print(stumo)
for i in range(N):
    print(stumo[i])
