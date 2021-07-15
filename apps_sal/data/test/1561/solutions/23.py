n, m, k = list(map(int, input().split()))
s = []
up = [[0] * m] * n
left =[[0] * m] * n
ans = 0
for i in range(n):
    s.append(input())
    for j in range(m):
        if s[i][j] == '.':
            up[i][j] = (0 if i == 0 else up[i - 1][j]) + 1
            left[i][j] = (0 if j == 0 else left[i][j - 1]) + 1
        else:
            up[i][j] = 0
            left[i][j] = 0
        ans += up[i][j] >= k
        ans += left[i][j] >= k
if k == 1:
    ans //= 2
print(ans)

