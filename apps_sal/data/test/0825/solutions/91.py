from itertools import groupby
import sys
from collections import Counter


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            table.append((i, cnt))
        i += 1
    if n > 1:
        table.append((n, 1))
    return table


input = sys.stdin.readline


def main():
    N = int(input())
    ans = 0
    table = prime_decomposition(N)
    for (_, cnt) in table:
        i = 1
        while cnt >= i:
            cnt -= i
            i += 1
            ans += 1
    print(ans)


main()
