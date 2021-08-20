(b1, q, l, m) = [int(i) for i in input().split()]
bad = [int(i) for i in input().split()]
if abs(q) > 1 and b1 != 0:
    b2 = b1
    count = 0
    while abs(b2) <= l:
        count += 1
        if b2 in bad:
            count -= 1
        b2 *= q
        '\n\tfor u in bad:\n\t\ti = u\n\n\t\twhile (i%q == 0):\n\t\t\ti = i / q\n\t\t\ta = i == b1\n\t\t\tif a:\n\t\t\t\tbreak\n\t\ta = i == b1\n\n\t\tif (a and abs(u)<=l) or u == b1:\n\t\t\tcount-=1\n\t'
    print(count)
else:
    '\n    if abs(b1)<=l:\n            if q == 1:\n                    if b1 in bad:\n                            print("0")\n                    else:\n                            print("inf")\n            elif q == 0:\n                    if 0 in bad:\n                            if b1 in bad:\n                                    print("0")\n                            else:\n                                    print("1")\n                    else:\n                            print("inf")\n            elif q == -1:\n                    if (b1 in bad) and (b2 in bad):\n                            print("0")\n                    else:\n                            print("inf")\n\n    else:\n            print("0")\n    '
    a1 = b1 * q
    if abs(b1) <= l:
        if b1 == 0:
            if b1 in bad:
                print('0')
            else:
                print('inf')
        elif a1 in bad:
            if b1 in bad:
                print('0')
            elif a1 == 0:
                print('1')
            else:
                print('inf')
        else:
            print('inf')
    else:
        print('0')
