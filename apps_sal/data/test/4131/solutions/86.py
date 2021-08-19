(N, M) = list(map(int, input().split()))
PY = [[list(map(int, input().split())), i] for i in range(M)]
PY.sort()
cnt = [0 for i in range(N + 1)]
ans = []
for i in range(M):
    cnt[PY[i][0][0]] += 1
    ans.append([PY[i][1], str(PY[i][0][0]).zfill(6) + str(cnt[PY[i][0][0]]).zfill(6)])
ans.sort()
for i in range(M):
    print(ans[i][1])
