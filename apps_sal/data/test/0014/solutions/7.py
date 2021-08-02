import sys
f = sys.stdin
n, k = map(int, f.readline().split())
s, t = [n + 1], 1
a = list(map(int, f.readline().split()))
for i in range(n):
    if i >= k:
        a += [s[-1] - 1]
    s += [a[i]]
    while (len(s) != 0) and (s[-1] == t):
        s.pop()
        t += 1
if len(s):
    print('-1')
else:
    print(' '.join(str(x) for x in a))
