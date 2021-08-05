import math
the_len = int(input())
s2 = input()
nums = s2.split(' ')

groups = [0] * 100001
max = 1

for n in nums:
    groups[int(n)] += 1

for i in range(2, 100001):
    res = 0
    for j in range(i, 100001, i):
        res += groups[j]
    if res > max:
        max = res

print(max)
