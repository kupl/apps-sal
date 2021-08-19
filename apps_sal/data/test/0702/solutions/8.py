def step(a, b):
    if a > n - 3 or b == 0 or b == n - 1 or l[a + 1][b] == '#' or l[a + 2][b] == '#' or l[a + 1][b - 1] == '#' or l[a + 1][b + 1] == '#':
        return False
    else:
        l[a] = l[a][:b] + '#' + l[a][b + 1:]
        l[a + 1] = l[a + 1][:b - 1] + '###' + l[a + 1][b + 2:]
        l[a + 2] = l[a + 2][:b] + '#' + l[a + 2][b + 1:]
        return True


n = int(input())
l = [input() for i in range(n)]
ans = 'YES'
for i in range(n):
    for j in range(n):
        if l[i][j] == '.' and not step(i, j):
            ans = 'NO'
print(ans)
