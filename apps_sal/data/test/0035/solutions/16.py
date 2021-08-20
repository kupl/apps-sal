(n, m) = list(map(int, input().split(' ')))
(ls, col) = ([], [])
for x in range(n):
    ls.append(input())
for i in range(m):
    elem = ''
    for x in ls:
        elem = ''.join([elem, x[i]])
    col.append(elem)


def ans():
    if n % 3 != 0 and m % 3 != 0:
        return 'NO'
    for x in ls:
        if any((y not in ['R', 'G', 'B'] for y in x)):
            return 'NO'
    if n % 3 == 0 and all((x == ls[0] for x in ls[0:n // 3])) and all((x == ls[n // 3] for x in ls[n // 3:2 * n // 3])) and all((x == ls[2 * n // 3] for x in ls[2 * n // 3:n])):
        if ls[0] != ls[n // 3] and ls[n // 3] != ls[2 * n // 3]:
            for z in ['R', 'G', 'B']:
                tmp = [bool(z in ls[0]), bool(z in ls[n // 3]), bool(z in ls[2 * n // 3])]
                if tmp.count(True) > 1:
                    return 'NO'
            return 'YES'
    if m % 3 == 0 and all((x == col[0] for x in col[0:m // 3])) and all((x == col[m // 3] for x in col[m // 3:2 * m // 3])) and all((x == col[2 * m // 3] for x in col[2 * m // 3:m])):
        if col[0] != col[m // 3] and col[m // 3] != col[2 * m // 3]:
            for z in ['R', 'G', 'B']:
                tmp = [bool(z in col[0]), bool(z in col[m // 3]), bool(z in col[2 * m // 3])]
                if tmp.count(True) > 1:
                    return 'NO'
            return 'YES'
    return 'NO'


print(ans())
