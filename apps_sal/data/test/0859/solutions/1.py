

import itertools
a = input()
b = input()

ap = a.count('+')
am = a.count('-')
bp = b.count('+')
bm = b.count('-')
bq = b.count('?')


if bq == 0:
    if ap == bp:
        print(1.0)
    else:
        print(0.0)
else:
    mas = list(itertools.product('+-', repeat=bq))
    if ap >= bp and am >= bm:
        ap -= bp
        am -= bm
        count = 0
        for el in mas:
            tmp_s = "".join(el)
            if tmp_s.count('+') == ap and tmp_s.count('-') == am:
                count += 1
        print(count / len(mas))
    else:
        print(0.0)

