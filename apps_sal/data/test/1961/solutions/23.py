n, m = list(map(int, input().split()))
a = [list('') for x in range(n)]
b = [list('.' * m) for x in range(n)]
start = 0
# end=n-2
for i in range(n):
    a[i] = list(input())
    if (start == 0):
        if ('.' in a[i]):
            start = ((i - 3) // 3) * 3
for i in range(start):
    b[i] = list('#' * m)
# print(start)
for i in range(start, n - 2):
    for j in range(m - 2):
        ok = True
        if a[i][j] == '#':
            for y in range(i, i + 3):
                if ok == False:
                    break
                for x in range(j, j + 3):
                    if not((y == i + 1) and (x == j + 1)):
                        if a[y][x] != '#':
                            # print('lel')
                            # print(x,y)
                            ok = False
                            break
            if ok:
                for y in range(i, i + 3):
                    for x in range(j, j + 3):
                        if not((y == i + 1) and (x == j + 1)):
                            b[y][x] = '#'

# for i in a:
#    print(i)
# print()
# for i in b:
#    print(i)

if a == b:
    print('YES')
else:
    print('NO')
