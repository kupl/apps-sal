n = int(input())
nums = [int(c) for c in input().split(' ')]
occur = {}
for num in nums:
    if num not in occur:
        occur[num] = 0
    occur[num] += 1
gcd = 1
for num in occur:
    if occur[num] == 2:
        gcd = max(gcd, num)
b = max(nums)
for num in occur:
    if b % num == 0:
        occur[num] -= 1
a = 1
for num in occur:
    if occur[num] == 1:
        a = max(a, num)
print(a, b)
