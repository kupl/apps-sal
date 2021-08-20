import functools


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def multiple(a, b):
    return a * b // euclid(a, b)


def lcm(nums):
    return functools.reduce(multiple, nums)


a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(lcm(a))
