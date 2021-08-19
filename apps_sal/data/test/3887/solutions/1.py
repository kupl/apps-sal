#!/usr/bin/env python3

import re

try:
    while True:
        s = input()
        n = int(s[s.rfind(' '):])
        pos = s.count('+') + 1
        neg = s.count('-')
        if n * pos - neg < n or pos - n * neg > n:
            print("Impossible")
        else:
            print("Possible")
            need = n - (pos - neg)
            prev = '+'
            first = True
            for m in re.finditer(r"[+-]", s):
                if first:
                    first = False
                else:
                    print(prev, end=' ')

                if prev == '+' and need > 0:
                    x = min(need + 1, n)
                    need -= x - 1
                elif prev == '-' and need < 0:
                    x = min(-need + 1, n)
                    need += x - 1
                else:
                    x = 1

                print(x, end=' ')
                prev = m.group()

            if not first:
                print(prev, end=' ')

            if prev == '+' and need > 0:
                x = min(need + 1, n)
                need -= x - 1
            elif prev == '-' and need < 0:
                x = min(-need + 1, n)
                need += x - 1
            else:
                x = 1

            print(x, '=', n)

except EOFError:
    pass
