def f():
    n = int(input())
    t = [list(input()) for i in range(n)]
    for i in range(n - 2):
        if t[i][0] == '#' or t[i][-1] == '#':
            return 'NO'
        for j in range(1, n - 1):
            if t[i][j] == '#':
                if '#' == t[i + 1][j - 1] == t[i + 1][j] == t[i + 1][j + 1] == t[i + 2][j]:
                    t[i + 1][j - 1] = t[i + 1][j] = t[i + 1][j + 1] = t[i + 2][j] = '.'
                else:
                    return 'NO'
    if '#' in t[-2] or '#' in t[-1]:
        return 'NO'
    return 'YES'


print(f())
