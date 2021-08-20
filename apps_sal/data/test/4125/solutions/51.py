import functools


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def gcd(nums):
    if len(nums) == 1:
        return nums[0]
    return functools.reduce(euclid, nums)


(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.append(k)
a.sort()
sa = []
for i in range(1, n + 1):
    sa.append(a[i] - a[i - 1])
print(gcd(sa))
