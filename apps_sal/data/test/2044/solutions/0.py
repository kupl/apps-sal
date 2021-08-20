import sys
import io
stream_enable = 0
inpstream = '\n3 5\n3 7 9\n\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


(n, m) = inpmap()
arr = inpmap()
s = 0
for x in arr:
    s += x
    print(s // m, end=' ')
    s %= m
print()
