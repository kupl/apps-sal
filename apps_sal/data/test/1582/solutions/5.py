N = int(input())
cnt = [[0] * 10 for i in range(10)]
for n in range(1, N + 1):
    cnt[int(str(n)[0])][int(str(n)[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
