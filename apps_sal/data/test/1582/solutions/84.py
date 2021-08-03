n = int(input())
cnt = [[0] * 10 for i in range(10)]
for i in range(1, n + 1):
    cnt[int(str(i)[0])][int(str(i)[-1])] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]
print(ans)
