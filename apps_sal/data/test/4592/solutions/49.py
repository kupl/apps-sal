import collections
import sys


def input():
    return sys.stdin.readline()


N = int(input())
d = collections.Counter()
if N == 1:
    print(1)
else:
    for n in range(2, N + 1):
        while n % 2 == 0:
            d[2] += 1
            n //= 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                while n % i == 0:
                    d[i] += 1
                    n //= i
            i += 2
        if n > 1:
            d[n] += 1
    ans = 1
    for (k, v) in d.items():
        ans = ans * (v + 1) % 1000000007
    print(ans)
