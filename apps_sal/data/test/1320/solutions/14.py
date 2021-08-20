n = int(input())
a = [0] * n
for i in range(n):
    a[i] = input().strip()
ans = 0
for i in range(n):
    s = 0
    for j in range(n):
        if a[i][j] == 'C':
            s += 1
    ans += s * (s - 1) // 2
for i in range(n):
    s = 0
    for j in range(n):
        if a[j][i] == 'C':
            s += 1
    ans += s * (s - 1) // 2
print(ans)
