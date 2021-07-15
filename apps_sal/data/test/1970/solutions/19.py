a = []


def first(i, j):
    nonlocal a
    a[i][j] = 1
    if i - 2 >= 0 and j + 2 < 8:
        a[i - 2][j + 2] = 1
    if i - 2 >= 0 and j - 2 >= 0:
        a[i - 2][j - 2] = 1
    if i + 2 < 8 and j + 2 < 8:
        a[i + 2][j + 2] = 1
    if i + 2 < 8 and j - 2 >= 0:
        a[i + 2][j - 2] = 1


def second(i, j):
    nonlocal a
    if a[i][j] == 1:
        return True
    if i - 2 >= 0 and j + 2 < 8:
        if a[i - 2][j + 2] == 1:
            return True
    if i - 2 >= 0 and j - 2 >= 0:
        if a[i - 2][j - 2] == 1:
            return True
    if i + 2 < 8 and j + 2 < 8:
        if a[i + 2][j + 2] == 1:
            return True
    if i + 2 < 8 and j - 2 >= 0:
        if a[i + 2][j - 2] == 1:
            return True
    return False


t = int(input())
for i in range(t):
    a = []
    exist = False
    for j in range(8):
        a.append(list(input()))
    d = 0
    for j in range(8):
        for k in range(8):
            if a[j][k] == 'K':
                d += 1
                if d == 1:
                    first(j, k)
                elif d == 2:
                    if second(j, k):
                        exist = True
    if exist:
        print("YES")
    else:
        print("NO")
    if i != t - 1:
        input()

