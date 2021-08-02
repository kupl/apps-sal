#!/usr/bin/env python3

LEVELS = ("hate", "love")

try:
    while True:
        n = int(input())
        s = []
        for i in range(n):
            if i:
                s += ["that"]
            s += ["I", LEVELS[i & 0x1]]

        print(' '.join(s + ["it"]))

except EOFError:
    pass
