(n, l, flag, o) = (int(input()), [], True, 0)
for i in range(n):
    l.append('0')
    l[i] = str(input())
for i in range(n):
    for el in range(n):
        if el - 1 >= 0:
            if l[i][el - 1] == 'o':
                o += 1
        if el + 1 < n:
            if l[i][el + 1] == 'o':
                o += 1
        if i - 1 >= 0:
            if l[i - 1][el] == 'o':
                o += 1
        if i + 1 < n:
            if l[i + 1][el] == 'o':
                o += 1
        flag &= o % 2 == 0
if flag:
    print('YES')
else:
    print('NO')
