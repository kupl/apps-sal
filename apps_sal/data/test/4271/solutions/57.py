N = int(input())
d = [[int(s) for s in input().split()] for i in range(3)]
ans = 0
for i in range(N):
    ans += d[1][d[0][i] - 1]
    if i <= N - 2 and d[0][i + 1] - d[0][i] == 1:
        ans += d[2][d[0][i] - 1]
print(ans)
