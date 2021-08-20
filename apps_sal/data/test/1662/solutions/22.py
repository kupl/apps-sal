from collections import Counter
n = int(input())
l = Counter((int(x) for x in input().split()))
a = []
b = []
for (x, y) in list(l.items()):
    a.append(x)
    if y > 1:
        b.append(x)
a.sort()
b.sort()
if len(b) and a[-1] == b[-1]:
    b = b[:-1]
ans = a + b[::-1]
print(len(ans))
print(' '.join((str(x) for x in ans)))
