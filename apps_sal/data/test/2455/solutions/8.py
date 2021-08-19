n = int(input())
for i in range(n):
    a = input()
    c = 0
    p = ''
    if 'XXXXXXXXXXXX' == a:
        print('6 1x12 2x6 3x4 4x3 6x2 12x1')
        continue
    if 'X' in a:
        p = p + '1x12'
        c += 1
        if 'XX' == a[0] + a[6] or 'XX' == a[1] + a[7] or 'XX' == a[2] + a[8] or ('XX' == a[3] + a[9]) or ('XX' == a[4] + a[10]) or ('XX' == a[5] + a[11]):
            c += 1
            p += ' 2x6'
        if 'XXX' == a[0] + a[4] + a[8] or 'XXX' == a[1] + a[5] + a[9] or 'XXX' == a[2] + a[6] + a[10] or ('XXX' == a[3] + a[7] + a[11]):
            p += ' 3x4'
            c += 1
        if 'XXXX' == a[0] + a[3] + a[6] + a[9] or 'XXXX' == a[1] + a[4] + a[7] + a[10] or 'XXXX' == a[2] + a[5] + a[8] + a[11]:
            c += 1
            p += ' 4x3'
        if 'XXXXXX' == a[0] + a[2] + a[4] + a[6] + a[8] + a[10] or 'XXXXXX' == a[1] + a[3] + a[5] + a[7] + a[9] + a[11]:
            c += 1
            p += ' 6x2'
        print(c, p)
    else:
        print(0)
