n = int(input())
a = [input() for i in range(n)]
if n == 1:
    print('YES')
else:
    ans = True
    c = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                c += int(a[i + 1][j] == 'o') + int(a[i][j + 1] == 'o')
            elif i == n - 1 and j == n - 1:
                c += int(a[i - 1][j] == 'o') + int(a[i][j - 1] == 'o')
            elif i == 0 and j == n - 1:
                c += int(a[i + 1][j] == 'o') + int(a[i][j - 1] == 'o')
            elif i == n - 1 and j == 0:
                c += int(a[i - 1][j] == 'o') + int(a[i][j + 1] == 'o')
            elif i == 0:
                c += int(a[i + 1][j] == 'o') + int(a[i][j + 1] == 'o') + int(a[i][j - 1] == 'o')
            elif i == n - 1:
                c += int(a[i - 1][j] == 'o') + int(a[i][j + 1] == 'o') + int(a[i][j - 1] == 'o')
            elif j == 0:
                c += int(a[i + 1][j] == 'o') + int(a[i - 1][j] == 'o') + int(a[i][j + 1] == 'o')
            elif j == n - 1:
                c += int(a[i + 1][j] == 'o') + int(a[i - 1][j] == 'o') + int(a[i][j - 1] == 'o')
            else:
                c += int(a[i + 1][j] == 'o') + int(a[i][j + 1] == 'o') + int(a[i][j - 1] == 'o') + int(a[i - 1][j] == 'o')
            if c % 2 != 0:
                ans = False
    print(['NO', 'YES'][ans])
