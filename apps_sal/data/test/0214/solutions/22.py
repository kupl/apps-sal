s1 = input()
s2 = input()
desk = [list(s1), list(s2)]
ln = len(s1)
ans = 0


def need(i):
    return [desk[0][i:i + 2], desk[1][i:i + 2]]


for i in range(ln - 1):
    if need(i) == [['0', '0'], ['0', '0']] or need(i) == [['0', '0'], ['0', 'X']]:
        desk[0][i] = 'X'
        desk[0][i + 1] = 'X'
        desk[1][i] = 'X'
    elif need(i) == [['0', '0'], ['X', '0']]:
        desk[0][i] = 'X'
        desk[0][i + 1] = 'X'
        desk[1][i + 1] = 'X'
    elif need(i) == [['0', 'X'], ['0', '0']]:
        desk[0][i] = 'X'
        desk[1][i] = 'X'
        desk[1][i + 1] = 'X'
    elif need(i) == [['X', '0'], ['0', '0']]:
        desk[0][i + 1] = 'X'
        desk[1][i] = 'X'
        desk[1][i + 1] = 'X'
    else:
        continue
    ans += 1
print(ans)
