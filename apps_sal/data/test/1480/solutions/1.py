import sys
3
(n, k) = list(map(int, sys.stdin.readline().split()))
a = [int(x) for x in sys.stdin.readline().split()]
l = [i for i in range(1, n + 1)]
p = 0
ret = []
for d in a:
    p += d
    p %= len(l)
    ret.append(l[p])
    del l[p]
print(' '.join((str(x) for x in ret)))
