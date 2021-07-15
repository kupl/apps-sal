i = int(input())
if i == 1:
    print(int(input()))
    print(0)
else:
    orig = [list(map(int, input().split(' '))) for a in range(i)]
    a = [[0]*i for _ in range(i)]
    b = [[0]*i for _ in range(i)]
    for x in range(i):
        a[x][x] = orig[x][x]

    for x in range(0, i):
       for y in range(x+1, i):
           a[x][y] = (orig[x][y]+orig[y][x])/2
           a[y][x] = (orig[x][y]+orig[y][x])/2
           b[x][y] = (orig[x][y]-orig[y][x])/2
           b[y][x] = -(orig[x][y]-orig[y][x])/2

    for i in a:
        print(' '.join([str(x) for x in i]))
    for i in b:
        print(' '.join([str(x) for x in i]))

