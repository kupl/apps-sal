x = int(input())
(h, m) = input().split()
if '7' in h + m:
    print(0)
else:
    res = 0
    while not '7' in h + m:
        m = str(int(m) - x)
        if m[0] == '-':
            m = str(60 + int(m))
            h = str(int(h) - 1)
            if h[0] == '-':
                h = str(24 + int(h))
        res += 1
    print(res)
