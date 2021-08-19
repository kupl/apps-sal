import sys
import math
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root + 1):
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
    D = defaultdict(int)
    if N == 1:
        print(1)
        return
    for n in range(2, N + 1):
        ND = prime_fact(n)
        for (p, a) in list(ND.items()):
            D[p] += a
    ans = 1
    for (p, a) in list(D.items()):
        ans = ans * (a + 1) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
