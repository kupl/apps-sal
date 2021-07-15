import sys

l = sys.stdin.readline().strip()
ls = len(l)

c = input()
c = int(c)

r = []

d = []

k = 0
d.append(0)
for i in range (0, ls - 1):
    if l[i] == l[i + 1]:
        k = k + 1
    d.append(k)

for i in range (0, c):
    (n, m) = sys.stdin.readline().strip().split(' ')
    n, m = int(n) - 1, int(m) - 1
    r.append(d[m] - d[n])

for s in r:
    print(s)

