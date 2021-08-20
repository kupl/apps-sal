from sys import stdin
import math
h = int(stdin.readline())
split_times = math.ceil(math.log2(h + 1))
sum_times = sum([2 ** i for i in range(split_times)])
print(sum_times)
