N, M = list(map(int, input().split()))

no = {}
ken = [[] for i in range(N)]
for i in range(M):
    p, y = list(map(int, input().split()))
    no[i] = str(p) + '_' + str(y)
    ken[p - 1].append(y)

ans = {}
for i in range(N):
    ken[i].sort()
    for j in range(len(ken[i])):
        ans[str(i + 1) + '_' + str(ken[i][j])] = str(i + 1).zfill(6) + str(j + 1).zfill(6)

for i in range(M):
    print((ans[no[i]]))
