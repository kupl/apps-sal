(n, m) = map(int, input().split())
num = ['.' * (m + 2)]
for i in range(n):
    s = '.'
    s += input()
    s += '.'
    num.append(s)
flag = True
num.append('.' * (m + 2))
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if num[i][j] == '.':
            if num[i - 1][j] != '*' and num[i - 1][j - 1] != '*' and (num[i - 1][j + 1] != '*') and (num[i][j - 1] != '*') and (num[i][j + 1] != '*') and (num[i + 1][j - 1] != '*') and (num[i + 1][j] != '*') and (num[i + 1][j + 1] != '*'):
                ans += 1
            else:
                flag = False
        if num[i][j] != '.' and num[i][j] != '*':
            x = int(num[i][j])
            if num[i - 1][j] == '*':
                x -= 1
            if num[i - 1][j - 1] == '*':
                x -= 1
            if num[i - 1][j + 1] == '*':
                x -= 1
            if num[i][j - 1] == '*':
                x -= 1
            if num[i][j + 1] == '*':
                x -= 1
            if num[i + 1][j - 1] == '*':
                x -= 1
            if num[i + 1][j] == '*':
                x -= 1
            if num[i + 1][j + 1] == '*':
                x -= 1
            if x != 0:
                flag = False
if not flag:
    print('NO')
else:
    print('YES')
