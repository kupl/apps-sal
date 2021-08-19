(N, M) = map(int, input().split())
student = [list(map(int, input().split())) for i in range(N)]
check = [list(map(int, input().split())) for i in range(M)]
tmp = []
for i in range(len(student)):
    for j in range(len(check)):
        x = abs(student[i][0] - check[j][0])
        y = abs(student[i][1] - check[j][1])
        tmp.append(x + y)
    print(tmp.index(min(tmp)) + 1)
    tmp = []
