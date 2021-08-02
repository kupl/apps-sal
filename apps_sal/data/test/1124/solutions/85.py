import functools
n = int(input())
a = list(map(int, input().split()))


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def gcd(nums):
    return functools.reduce(euclid, nums)


print(gcd(a))
