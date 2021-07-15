from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

T = ni()
for _ in range(T):
    N = ni()
    lp, lc = 0, 0
    fail = False
    for _ in range(N):
        p, c = nl()
        dp = p - lp
        dc = c - lc
        lp, lc = p, c
        if dp < dc or dc < 0:
            fail = True
    if fail:
        print('NO')
    else:
        print('YES')
    


