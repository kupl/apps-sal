n = int(input())
s = []
count = 0
for i in range(n):
    s.append(list(input()))
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if s[i][j] == 'X' and s[i - 1][j - 1] == 'X' and s[i + 1][j - 1] == 'X' and s[i - 1][j + 1] == 'X' and s[i + 1][j + 1] == 'X':
            count += 1
print(count)
