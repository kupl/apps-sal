def test_achiral(ch, achiral):
    for i in ch:
        if i in achiral:
            print('NO')
            return ()
    ch1 = ''
    j = -1
    while j >= -len(ch):
        ch1 = ch1 + ch[j]
        j -= 1
    if ch1 == ch:
        print('YES')
        return ()
    else:
        print('NO')
        return ()


achiral = 'BCDEFGJKLNPQRSZ'
ch = input()
test_achiral(ch, achiral)
