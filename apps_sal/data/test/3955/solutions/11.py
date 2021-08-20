import sys
import math
[n, k, x] = [int(i) for i in sys.stdin.readline().rstrip('\n').split()]
nums = [int(i) for i in sys.stdin.readline().rstrip('\n').split()]
offset = 1
for i in range(k):
    offset = offset * x
leftor = [0]
for i in nums[:-1]:
    leftor.append(leftor[-1] | i)
rightor = [0]
for i in range(len(nums) - 1, 0, -1):
    rightor.append(rightor[-1] | nums[i])
ans = []
for i in range(len(nums)):
    ans.append(leftor[i] | (nums[i] * offset | rightor[n - i - 1]))
sys.stdout.write(str(max(ans)) + '\n')
