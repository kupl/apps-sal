n = int(input())
ans = [[0] * 9 for _ in range(9)]
for i in range(1, n + 1):
    s = str(i)
    if s[0] != "0" and s[-1] != "0":
        ans[int(s[0]) - 1][int(s[-1]) - 1] += 1
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        cnt += ans[i - 1][j - 1] * ans[j - 1][i - 1]
print(cnt)
