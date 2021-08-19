import sys
nums = sys.stdin.readline().split(' ')
n = int(nums[0])
x = int(nums[1])
current = 1
total = 0
for i in range(n):
    next = sys.stdin.readline().split(' ')
    next_l = int(next[0])
    next_r = int(next[1])
    total += next_r - next_l + 1 + (next_l - current) % x
    current = (next_r + 1) % x
print(total)
