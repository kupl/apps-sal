import sys


def I():
    return sys.stdin.readline().rstrip()


n = int(I())
s = I()
l = []
cc = 'c'
for c in s:
    if c == cc:
        l[-1] += 1
    else:
        l.append(1)
    cc = c

ans = (n * (n - 1)) // 2
for i in range(len(l)):
    if i > 0:
        ans -= l[i] - 1
    if i < len(l) - 1:
        ans -= l[i]

print(ans)
