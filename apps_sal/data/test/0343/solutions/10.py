(n, k, p, x, y) = map(int, input().split())
V = list(map(int, input().split()))
suma = sum(V)
smaller = 0
for num in V:
    if num < y:
        smaller += 1
if smaller >= (n + 1) / 2:
    print('-1')
else:
    no1 = (n + 1) / 2 - smaller - 1
    no1 = int(no1)
    noy = n - k - no1
    if no1 < 0:
        noy += no1
        no1 = 0
    elif noy < 0:
        no1 += noy
        noy = 0
    if suma + no1 + y * noy > x:
        print('-1')
    else:
        print('1 ' * no1 + '{} '.format(y) * noy)
