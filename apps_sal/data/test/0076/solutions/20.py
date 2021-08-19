import sys
import io
stream_enable = 0
inpstream = '\n2 7 3 7\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


(n, m, a, b) = inpmap()
x = n % m * b
y = (m - n % m) * a
print(min(x, y))
