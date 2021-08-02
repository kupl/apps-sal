import math
N = int(input())
A = list(map(int, input().split()))


def gcd_list(nums):
    gcd = nums[0]
    for i in range(1, len(nums)):
        gcd = math.gcd(gcd, nums[i])
    return gcd


print(gcd_list(A))
