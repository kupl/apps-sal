import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    N = NI()
    PD = {}
    for i in range(2, N+1):
        pd = prime_fact(i)
        for p, k in pd.items():
            PD.setdefault(p, 0)
            PD[p] += k
    X = {74: 0, 24: 0, 14: 0, 4: 0, 2: 0}
    for p, k in PD.items():
        for x in X.keys():
            if k >= x:
                X[x] += 1
    print(X[74] + X[24]*(X[2]-1) + X[14]*(X[4]-1) + X[4]*(X[4]-1)//2 * (X[2]-2))


def __starting_point():
    main()
__starting_point()
