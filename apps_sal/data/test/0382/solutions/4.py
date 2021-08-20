import sys
import io
stream_enable = 0
inpstream = '\n15 2 3\nabacabadabacaba\nba\n1 15\n3 4\n2 14\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


(n, m, q) = inpmap()
a = input()
b = input()
s = [0] * n
s[0] = int(a.startswith(b))
for i in range(1, n):
    s[i] = s[i - 1] + int(a[i:i + m] == b)
for i in range(q):
    (x, y) = inpmap()
    r = (s[y - m] if y - m >= 0 else 0) - (s[x - 2] if x - 2 >= 0 else 0)
    print(max(r, 0))
