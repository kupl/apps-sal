from collections import defaultdict
nums = None
with open("input.txt") as f:
    n = next(f)
    line = next(f)
    nums = [int(i) for i in line.split()]
non_neg = defaultdict(int)
non_pos = defaultdict(int)
for i, num in enumerate(nums):
    if num >= 0:
        non_neg[i] = non_neg[i - 1] + 1
    else:
        non_neg[i] = non_neg[i - 1]


for i in range(len(nums) - 1, -1, -1):
    num = nums[i]
    if num <= 0:
        non_pos[i] = 1 + non_pos[i + 1]
    else:
        non_pos[i] = non_pos[i + 1]

res = float("inf")
for i, num in enumerate(nums[:len(nums) - 1]):
    res = min(non_neg[i] + non_pos[i + 1], res)

with open("output.txt", 'a') as f:
    f.write(str(res))
