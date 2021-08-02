from fractions import gcd
a = int(input())
nums = list(map(int, input().split(' ')))
gcdx = nums[0]
for i in range(len(nums)):
    gcdx = gcd(gcdx, nums[i])
print(gcdx * a)
