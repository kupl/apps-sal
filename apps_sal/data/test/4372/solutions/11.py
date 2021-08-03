from functools import reduce


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


n = int(input())
arr = [int(x) for x in input().split(' ')]
mx = max(arr)
arr = [mx - x for x in arr if mx - x]
GCD = reduce(gcd, arr)
print(sum(arr) // GCD, GCD)
