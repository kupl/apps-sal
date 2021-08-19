import sys
(n, m) = [int(x) for x in sys.stdin.readline().split()]
if n % m == 0:
    print(' '.join([str(int(n / m))] * m))
else:
    v = [str(int(n / m))] * (m - n % m)
    v.extend([str(int(n / m) + 1)] * (n % m))
    print(' '.join(v))
