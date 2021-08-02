from functools import reduce
N = int(input())
L = list(map(int, input().split()))


def gcd(A, B):
    if A < B:
        A, B = B, A

    while B:
        A, B = B, A % B
    return A


print((reduce(gcd, L)))
