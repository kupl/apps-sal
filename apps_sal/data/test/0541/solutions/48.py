(N, M) = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(M)]
ans = 0
ab.sort(key=lambda x: x[1])
recent_cut = -1
for i in range(M):
    if recent_cut < ab[i][0]:
        recent_cut = ab[i][1] - 1
        ans += 1
print(ans)
