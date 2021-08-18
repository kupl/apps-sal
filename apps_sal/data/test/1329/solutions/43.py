import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7


def cal_divisors(N):
    divisors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
        i += 1
    divisors.sort()
    return divisors


def prime_factorize(N):
    prime_list = []
    while N % 2 == 0:
        prime_list.append(2)
        N //= 2
    f = 3
    while f**2 <= N:
        if N % f == 0:
            prime_list.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        prime_list.append(N)
    return prime_list


def main():
    N = int(input())
    divisors = []
    for i in range(1, N + 1):
        divisors.extend(prime_factorize(i))
    l = Counter(divisors)
    ans = 0
    nums = list(l.values())
    ans += len([*[x for x in nums if x >= 74]])

    ans += len([*[x for x in nums if x >= 14]]) * (len([*[x for x in nums if x >= 4]]) - 1)

    ans += len([*[x for x in nums if x >= 24]]) * (len([*[x for x in nums if x >= 2]]) - 1)

    ans += len([*[x for x in nums if x >= 4]]) * (len([*[x for x in nums if x >= 4]]) - 1) * (len([*[x for x in nums if x >= 2]]) - 2) // 2

    print(ans)


def __starting_point():
    main()


__starting_point()
