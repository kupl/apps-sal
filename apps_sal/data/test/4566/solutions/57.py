
N, M = list(map(int, input().split()))
# 都市Aと都市Bを結ぶ路線M
A_B = [list(map(int, input().split())) for _ in range(M)]
ans = [0] * N

for a, b in A_B:
    ans[a-1] += 1
    ans[b-1] += 1
for a in ans:
    print(a)

