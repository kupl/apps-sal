import sys

n, m, a, b = [int(x) for x in sys.stdin.readline().split()]
if b / m >= a:
    print(n * a)
else:
    res = b * (n // m)
    if (n % m) * a < b:
        res += (n % m) * a
    else:
        res += b
    print(res)
