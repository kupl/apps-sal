from functools import reduce
from operator import add

N = int(input())
A = list(map(int, input().split()))


def cum(total, a):
    total.append(a + total[-1])
    return total


cumsum = reduce(cum, A, [0])
cum_last = cumsum[-1]

p = 1000000007


def i_fixed(i):
    return (A[i] * (cum_last - cumsum[i + 1])) % p


def solve():
    return map(i_fixed, range(N - 1))


print(sum(solve()) % p)
