n = int(input())
l = [list(input()) for i in range(n)]
rows = [0 for i in range(n)]
cols = [0 for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if l[i][j] == 'C':
            rows[i] += 1
            cols[j] += 1
for i in range(n):
    ans += max(0, rows[i] * (rows[i] - 1) / 2)
    ans += max(0, cols[i] * (cols[i] - 1) / 2)
print(int(ans))
