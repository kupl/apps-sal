import sys
import math
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
a = [1] * n
for c in s:
    if c != '0':
        a[0] = 0
for k in range(1, n):
    if n % k == 0:
        t = [0] * k
        for (i, c) in enumerate(s):
            if c != '0':
                t[i % k] += 1
        if sum([_ % 2 for _ in t]) != 0:
            a[k] = 0
    else:
        a[k] = a[math.gcd(n, k)]
sys.stdout.write('{0}\n'.format(sum(a)))
