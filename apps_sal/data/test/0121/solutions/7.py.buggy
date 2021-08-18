def get_field(i, j, val):
    if i < 0 or j < 0 or i > 3 or j > 3:
        return False
    return d[i][j] == val


def check_field(i, j, c):
    if get_field(i - 2, j, c) and get_field(i - 1, j, c):
        return True
    if get_field(i + 2, j, c) and get_field(i + 1, j, c):
        return True
    if get_field(i, j - 2, c) and get_field(i, j - 1, c):
        return True
    if get_field(i, j + 2, c) and get_field(i, j + 1, c):
        return True
    if get_field(i - 1, j, c) and get_field(i + 1, j, c):
        return True
    if get_field(i, j - 1, c) and get_field(i, j + 1, c):
        return True

    if get_field(i + 2, j + 2, c) and get_field(i + 1, j + 1, c):
        return True
    if get_field(i - 2, j - 2, c) and get_field(i - 1, j - 1, c):
        return True
    if get_field(i + 2, j - 2, c) and get_field(i + 1, j - 1, c):
        return True
    if get_field(i - 2, j + 2, c) and get_field(i - 1, j + 1, c):
        return True
    if get_field(i + 1, j + 1, c) and get_field(i - 1, j - 1, c):
        return True
    if get_field(i - 1, j + 1, c) and get_field(i + 1, j - 1, c):
        return True


d = [[''] * 4 for i in range(4)]
for i in range(4):
    s = input()
    for j in range(4):
        d[i][j] = s[j]
for i in range(4):
    for j in range(4):
        if d[i][j] == '.':
            if check_field(i, j, 'x'):
                print("YES")
                return
print("NO")
