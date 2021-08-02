import re
import sys

n, m = list(map(int, input().split()))

s = sys.stdin.read()
d = s.split('\n')
d.remove("")
rgb = "RGB"
f = True
# print(s)
# print(d)
for c in rgb:
    t = re.findall(c + "+", d[0])
    if len(t) != 1 or len(t[0]) != m / 3:
        f = False

if f:
    for st in d:
        if st != d[0]:
            f = False

if f:
    print("YES")
    return

s = s.replace('\n', '')
f = True
for c in rgb:
    t = re.findall(c + "+", s)
    if len(t) != 1 or len(t[0]) != m * n / 3:
        f = False

if f:
    print("YES")
    return

print("NO")
