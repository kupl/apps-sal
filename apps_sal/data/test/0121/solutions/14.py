b = [list(input().strip()) for _ in range(4)]
r = 'NO'


def check(b):
    for i in range(4):
        for j in range(2):
            if b[i][j] == 'x' and b[i][j + 1] == 'x' and (b[i][j + 2] == 'x'):
                return True
    for i in range(2):
        for j in range(4):
            if b[i][j] == 'x' and b[i + 1][j] == 'x' and (b[i + 2][j] == 'x'):
                return True
    for i in range(2):
        for j in range(2):
            if b[i][j] == 'x' and b[i + 1][j + 1] == 'x' and (b[i + 2][j + 2] == 'x'):
                return True
    for i in range(2):
        for j in range(2, 4):
            if b[i][j] == 'x' and b[i + 1][j - 1] == 'x' and (b[i + 2][j - 2] == 'x'):
                return True
    return False


for i in range(4):
    for j in range(4):
        c = b[i][j]
        if c == '.':
            b[i][j] = 'x'
            if check(b):
                r = 'YES'
            b[i][j] = '.'
print(r)
