n = int(input())
cnt = [[0] * 9 for _ in range(9)]
for i in range(1, n + 1):
    s = str(i)
    if s[-1] != '0':
        cnt[int(s[0]) - 1][int(s[-1]) - 1] += 1
ans = 0
for i in range(9):
    for j in range(9):
        ans += cnt[i][j] * cnt[j][i]
print(ans)
