from bisect import bisect_left, bisect_right
from sys import stdin, stdout, setrecursionlimit
from collections import Counter
def input(): return stdin.readline().strip()


print = stdout.write

mod = 998244353

n, m, L, R = map(int, input().split())
if (n * m) % 2:
    print(str(pow(R - L + 1, n * m, mod)) + '\n')
else:
    nm = n * m
    if L % 2 and R % 2:
        even = (R - L) // 2
    elif L % 2 and not R % 2:
        even = (R - L + 1) // 2
    elif not L % 2 and R % 2:
        even = (R - L + 1) // 2
    else:
        even = (R - L) // 2 + 1
    odd = (R - L + 1) - even
    N = (pow(odd + even, nm, mod) + pow(abs(odd - even), nm, mod)) % mod
    print(str((pow(2, mod - 2, mod) * N) % mod) + '\n')
