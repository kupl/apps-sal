from collections import deque

n = int(input().strip())
nums = list(map(int, input().strip().split()))
nums = sorted([abs(num) for num in nums], reverse=True)

res = 0
max_index = 0
curr_index = 1
for curr_index in range(1, n):
    while nums[curr_index] * 2 < nums[max_index]:
        max_index += 1
    res += curr_index - max_index
print(res)
