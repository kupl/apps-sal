from itertools import groupby

n = int(input())

nums = [int(i) for i in input().split()]
copy = list(nums)

pos = input()


pos = ["".join(g) for k, g in groupby(pos) if k != '#']

# print(pos)

cur_pos = 0

for i in pos:
    if i[0] == '1':
        nums[cur_pos:cur_pos + len(i) + 1] = sorted(nums[cur_pos:cur_pos + len(i) + 1])
    cur_pos += len(i)

if sorted(copy) == nums:
    print("YES")
else:
    print("NO")
