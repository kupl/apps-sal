(n, m) = map(int, input().split())
lines = [input() for i in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(m - 1):
        a = lines[i][j] + lines[i + 1][j] + lines[i][j + 1] + lines[i + 1][j + 1]
        if 'f' in a and 'a' in a and ('c' in a) and ('e' in a):
            ans += 1
print(ans)
