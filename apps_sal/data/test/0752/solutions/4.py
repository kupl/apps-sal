import sys
import io
stream_enable = 0
inpstream = '\n3\nXS\nXS\nM\nXL\nS\nXS\n'
if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
m = 0
for x in a:
    if x in b:
        b.remove(x)
    else:
        m += 1
print(m)
