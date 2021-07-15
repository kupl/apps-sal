t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    possible = ['Ya', 'Ya', 'Ya', 'Ya']
    if (a+b)%2 == 0:
        possible[0] = 'Tidak'
        possible[1] = 'Tidak'
    else:
        possible[2] = 'Tidak'
        possible[3] = 'Tidak'
    if (a+d) == 0:
        possible[0] = 'Tidak'
        possible[3] = 'Tidak'
    if (b+c) == 0:
        possible[1] = 'Tidak'
        possible[2] = 'Tidak'

    print(' '.join(possible))

