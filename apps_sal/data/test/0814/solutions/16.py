from sys import stdin
inp = stdin
inp.readline()
nums = [int(x) for x in inp.readline().strip().split()]
nums.sort()
nums = [str(x) for x in nums]
print(' '.join(nums))
