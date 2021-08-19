(r, c) = [int(x) for x in input().split()]
table = [[c for c in input()] for i in range(r)]


def check(i, j):
    if i > 0:
        if table[i - 1][j] == 'W':
            return False
    if i < r - 1:
        if table[i + 1][j] == 'W':
            return False
    if j > 0:
        if table[i][j - 1] == 'W':
            return False
    if j < c - 1:
        if table[i][j + 1] == 'W':
            return False
    return True


no = False
for i in range(r):
    for j in range(c):
        if table[i][j] == 'S' and check(i, j) is False:
            print('No')
            no = True
            break
    if no:
        break
if not no:
    print('Yes')
    for i in range(r):
        s = ''
        for j in range(c):
            s += 'D' if table[i][j] == '.' else table[i][j]
        print(s)
