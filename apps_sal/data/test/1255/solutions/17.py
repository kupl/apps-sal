import sys

n = int(eval(input()))

c = 1
a = [0] * 60 * 24

for i in range(n):
    nums = list(map(int, input().split()))
    a[nums[0] * 60 + nums[1]] += 1

for i in range(60 * 24):
    c = max(c, a[i])

print(c)
