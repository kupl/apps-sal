def sol():
    s = input()
    on = 0
    zr = 0
    tot = 0
    for n in s:
        if n == '1':
            if zr == 0:
                on += 1
            else:
                zr -= 1
                tot += 1
        elif on == 0:
            zr += 1
        else:
            on -= 1
            tot += 1
    if tot % 2:
        print('DA')
    else:
        print('NET')


for n in range(int(input())):
    sol()
