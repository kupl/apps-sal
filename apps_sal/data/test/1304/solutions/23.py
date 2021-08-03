g = [[], [], [], [], [], [], [], [], []]
for i in range(3):
    s = input().split()
    g[0].append((' '.join(j for j in s[0])).split())
    g[1].append((' '.join(j for j in s[1])).split())
    g[2].append((' '.join(j for j in s[2])).split())
la = input()
for i in range(3):
    s = input().split()
    g[3].append((' '.join(j for j in s[0])).split())
    g[4].append((' '.join(j for j in s[1])).split())
    g[5].append((' '.join(j for j in s[2])).split())
la = input()
for i in range(3):
    s = input().split()
    g[6].append((' '.join(j for j in s[0])).split())
    g[7].append((' '.join(j for j in s[1])).split())
    g[8].append((' '.join(j for j in s[2])).split())
z = input().split()
z[0] = int(z[0])
z[1] = int(z[1])
z[0] %= 3
z[1] %= 3
x = z[0]
y = z[1]
ref = 0
if x == 1 and y == 1:
    ref = 0
if x == 1 and y == 2:
    ref = 1
if x == 1 and y == 0:
    ref = 2

if x == 2 and y == 1:
    ref = 3
if x == 2 and y == 2:
    ref = 4
if x == 2 and y == 0:
    ref = 5

if x == 0 and y == 1:
    ref = 6
if x == 0 and y == 2:
    ref = 7
if x == 0 and y == 0:
    ref = 8


def check(g):
    for i in g:
        for j in i:
            if j == '.':
                return True
    return False


if check(g[ref]):
    for i in range(3):
        for j in range(3):
            if(g[ref][i][j] == '.'):
                g[ref][i][j] = '!'
else:
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if(g[i][j][k] == '.'):
                    g[i][j][k] = '!'

ans = ''
for i in range(3):
    for j in range(3):
        ans += g[i][0][j]
    ans += ' '
print(ans)
ans = ''
for i in range(3):
    for j in range(3):
        ans += g[i][1][j]
    ans += ' '
print(ans)
ans = ''
for i in range(3):
    for j in range(3):
        ans += g[i][2][j]
    ans += ' '
print(ans)
ans = ''
print()
for i in range(3, 6, 1):
    for j in range(3):
        ans += g[i][0][j]
    ans += ' '
print(ans)
ans = ''
for i in range(3, 6, 1):
    for j in range(3):
        ans += g[i][1][j]
    ans += ' '
print(ans)
ans = ''
for i in range(3, 6, 1):
    for j in range(3):
        ans += g[i][2][j]
    ans += ' '
print(ans)
ans = ''
print()
for i in range(6, 9, 1):
    for j in range(3):
        ans += g[i][0][j]
    ans += ' '
print(ans)
ans = ''
for i in range(6, 9, 1):
    for j in range(3):
        ans += g[i][1][j]
    ans += ' '
print(ans)
ans = ''
for i in range(6, 9, 1):
    for j in range(3):
        ans += g[i][2][j]
    ans += ' '
print(ans)
