s = [input().strip() for i in range(8)]
d1 = []
d2 = []


def check(x, y):
    if s[x][y] == 'B':
        for i in range(x + 1, 8):
            if s[i][y] == 'W':
                return False
    elif s[x][y] == 'W':
        for i in range(x - 1, -1, -1):
            if s[i][y] == 'B':
                return False
    return True


for i in range(8):
    for j in range(8):
        if s[i][j] == 'B' and check(i, j):
            d1.append(8 - i - 1)
        elif s[i][j] == 'W' and check(i, j):
            d2.append(i)
if min(d1) < min(d2):
    print('B')
else:
    print('A')
