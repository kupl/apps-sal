n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    xx = 2 * b - a
    if xx < 0 or xx % 3 != 0:
        print('NO')
        continue
    x = xx // 3
    y = b - 2 * x
    if y < 0:
        print('NO')
        continue
    print('YES')
