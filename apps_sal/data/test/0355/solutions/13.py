field = [input() for i in range(8)]
field = [[field[y][x] for y in range(8)] for x in range(8)]

wa = float('+inf')
wb = float('+inf')


for row in field:
    row = ''.join(row)
    if 'W' in row:
        if ('B' in row) and row.index('W') > row.index('B'):
            pass
        else:
            nwa = row.index('W')
            wa = min(wa, nwa)
    if 'B' in row:
        if ('W' in row) and row.rindex('W') >  row.rindex('B'):
            pass
        else:
            nwb = 7 - row.rindex('B')
            wb = min(wb, nwb)


if wa <= wb:
    print('A')
else:
    print('B')

