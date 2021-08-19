import sys
lines = iter(sys.stdin.read().split('\n'))
n = int(next(lines))
nums = list(map(int, next(lines).strip(' ').split(' ')))
total = 0
count = 0
turns = -1
direction = 1


def traverse(nums, direction, total, count):
    """direction - 0: left to right, 1: right to left"""
    if direction == 0:
        for (i, num) in enumerate(nums):
            if num != -1 and num <= total:
                count += 1
                total += 1
                nums[i] = -1
    elif direction == 1:
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num != -1 and num <= total:
                count += 1
                total += 1
                nums[i] = -1
    return (total, count)


while count < n:
    turns += 1
    direction = 1 - direction
    (total, count) = traverse(nums, direction, total, count)
print(turns)
