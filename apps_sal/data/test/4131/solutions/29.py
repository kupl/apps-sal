N, M = list(map(int, input().split()))

C = []
for i in range(M):
    p, y = list(map(int, input().split()))
    C.append([i, p, y])
C.sort(key=lambda x: (x[1], x[2]))

ans = []
k = C[0][1]
n = 1
for i in range(M):
    city = C[i][1]
    if k != city:
        k = city
        n = 1
    number = f'{city:06}{n:06}'
    ans.append([C[i][0], number])
    n += 1
ans.sort(key=lambda x: x[0])
for i in range(M):
    print((ans[i][1]))
