from heapq import heapify, heappop, heappush
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product
from collections import deque
from math import ceil, floor, log2
import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())


def MI(): return list(map(int, input().split()))
def MI1(): return list(map(int1, input().split()))


def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def SI(): return input().split()


def printlist(lst, k='\n'): print((k.join(list(map(str, lst)))))


INF = float('inf')


def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i:
            continue
        ex = 0
        while n % i == 0:
            n = n // i
            ex += 1
        res.append((i, ex))
    if n != 1:
        res.append((n, 1))
    return res


def mcomb(n, k, mod):
    def mfac(l, r, mod):
        ans = l
        for i in reversed(list(range(r, l))):
            ans *= i
            ans %= mod
        return ans

    A = mfac(n, n - k + 1, mod)
    B = mfac(k, 1, mod)
    # B = mpow(B,mod-2,mod)
    B = pow(B, mod - 2, mod)
    return A * B % mod


def solve():
    n, m = MI()
    fact = prime_factorization(m)
    if n == 1:
        print((1))
        return
    # print(fact)
    mod = 1000000007
    ans = 1
    for num, ex in fact:
        # print(ex, mcomb(ex+n-2, n-1, mod))
        ans *= mcomb(ex + n - 1, n - 1, mod) % mod
    print((ans % mod))


def __starting_point():
    solve()


__starting_point()
