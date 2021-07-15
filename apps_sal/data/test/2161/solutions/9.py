n = int(input())
directory = dict()
for _ in range(n):
    name, k, *nums = input().split()
    if name in directory:
        directory[name] += nums
    else:
        directory[name] = nums

print(len(directory.keys()))
for name in directory:
    nums = directory[name]
    nums.sort(key=len)
    new_list = []
    for ind, num in enumerate(nums):
        l = len(num)
        if all(_num[-l:] != num for _num in nums[ind + 1:]):
            new_list.append(num)
    print(name, len(new_list), *new_list)
