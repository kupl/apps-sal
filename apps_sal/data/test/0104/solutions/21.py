import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nsum = sum(nums) / 2
csum = 0
for i in range(n):
    csum += nums[i]
    if csum >= nsum:
        print(i + 1)
        break
