(N, M) = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]
ans = [0] * (M + 1)
for i in range(N):
    for j in range(l[i][0]):
        ans[l[i][j + 1]] += 1
print(ans.count(N))
