import sys
import io

stream_enable = 0

inpstream = """
2 3
2 9
5 3 13
"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()

def inpmap():
    return list(map(int, input().split()))

n, m = inpmap()
a = inpmap()
b = inpmap()
x = b[-1]
for t in a[:-1]:
    x ^= t
y = a[-1]
for t in b[:-1]:
    y ^= t
if (x == y):
    print("YES")
else:
    print("NO")
    return
for i in range(n - 1):
    print("0 " * (m - 1), end='')
    print(a[i])
print(*b[:-1], end=(' ' if len(b) > 1 else ''))
print(x)

