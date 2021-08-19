n = int(input())
a = [[0] * n for i in range(n)]
ans = 'YES'
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == '#':
            a[i][j] = 1
# print(a)
for i in range(n - 2):
    for j in range(1, n - 1):
        if a[i][j] == 1:
            if a[i + 1][j] == 1 and a[i + 2][j] == 1 and a[i + 1][j - 1] == 1 and a[i + 1][j + 1] == 1:
                a[i][j] = 0
                a[i + 1][j] = 0
                a[i + 2][j] = 0
                a[i + 1][j - 1] = 0
                a[i + 1][j + 1] = 0
            else:
                ans = 'NO'
# print(a)
for i in range(n):
    if sum(a[i]) != 0:
        ans = 'NO'
print(ans)
