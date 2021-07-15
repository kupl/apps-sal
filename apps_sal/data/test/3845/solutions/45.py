a, b = list(map(int, input().split()))

print('100 100')

flip = a > b

if flip:
    a, b = b, a

f = [['#' for _ in range(100)] for __ in range(100)]

i, j = (0, 0)

for _ in range(b-1):
    f[i][j+1] = '.'
    f[i+1][j+1] = '.'
    f[i+1][j] = '.'

    j += 2

    if j > 98:
        j = 0
        i += 2

i, j = (99, 0)

if b == 1:
    a += 1

for _ in range(a-1):
    f[i][j] = '.'
    j += 2

    if j > 98:
        j = 0
        i -= 2

if flip:
    for i in range(100):
        f[i] = list(['.' if x == '#' else '#' for x in f[i]])

for row in f:
    print((''.join(row)))

