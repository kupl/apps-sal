from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

mod = 998244353
def solve():
    n, k = rl()
    if k > n:
        print(0)
        return
    elif k == 1:
        print (n)
        return

    f = [1]
    fi = [1]
    for i in range(1, n + 1):
        f.append((f[-1]*i)%mod)
        fi.append((fi[-1] * modinv(i, mod))%mod)

    def C(a,b):
        return f[a]*fi[b]*fi[a-b]

    d = n
    i = 1
    answer = 0
    while d >= k:
        answer = (answer + C(d - 1, k - 1)) % mod
        i += 1
        d = n // i
    print (answer)


mode = 'S'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

