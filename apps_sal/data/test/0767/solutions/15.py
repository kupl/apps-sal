"""
Created on Fri Apr  5 21:33:01 2019

@author: Z

4
abcd
gg
codeforces
abaca


"""
from fractions import gcd
from collections import Counter


def main():
    (n, z) = [int(a) for a in input().split()]
    nums = [int(a) for a in input().split()]
    nums.sort()
    if n % 2 == 0:
        x1 = nums[:n // 2]
        x2 = nums[n // 2:]
    else:
        x1 = nums[:n // 2]
        x2 = nums[n // 2 + 1:]
    n = n // 2
    cnt = 0
    i = 0
    j = 0
    while i < n and j < n:
        while j < n and x2[j] < x1[i] + z:
            j += 1
        if j < n:
            cnt += 1
            i += 1
            j += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
