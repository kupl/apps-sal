import sys
import io
stream_enable = 0
inpstream = '\n3 6 2 3 3\n1 2 1 3\n1 4 3 4\n1 2 2 3\n\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


(n, h, a, b, k) = inpmap()
for i in range(k):
    (ta, fa, tb, fb) = inpmap()
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
