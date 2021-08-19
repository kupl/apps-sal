import functools


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def gcd(nums):
    return functools.reduce(euclid, nums)


n = int(input())
a = [int(i) for i in input().split()]
print(gcd(a))
