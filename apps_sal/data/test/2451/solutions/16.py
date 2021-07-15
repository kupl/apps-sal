import sys
import io

stream_enable = 0

inpstream = """
3 6 2 3 3
1 2 1 3
1 4 3 4
1 2 2 3

"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()

def inpmap():
    return list(map(int, input().split()))

n, h, a, b, k = inpmap()
for i in range(k):
    ta, fa, tb, fb = inpmap()
    r = 0
    if ta != tb:
        if fa > b:
            r += fa - b
            fa = b
        if fa < a:
            r += a - fa
            fa = a
    r += abs(ta - tb)
    r += abs(fa - fb)
    print(r)

