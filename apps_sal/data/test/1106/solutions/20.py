import sys
import os
import fileinput
n = int(input()) + 1
a = [int(x) for x in input().split()]
all_count = 2 ** n - 1
b = [0] * all_count
counter = 0
for i in range(n, 1, -1):
    lcnt = 2 ** (i - 1)
    first = 2 ** (i - 1) - 2
    level = a[first:first + lcnt]
    for j in range(0, lcnt, 2):
        index = first + 2 + j
        if i == n:
            diff = abs(level[j] - level[j + 1])
            counter += diff
            b[index // 2 - 1] += level[j] + level[j + 1] + diff
        else:
            diff = abs(abs(b[index - 1] // 2 + level[j]) - abs(b[index] // 2 + level[j + 1]))
            counter += diff
            b[index // 2 - 1] += b[index - 1] // 2 + b[index] // 2 + level[j] + level[j + 1] + diff
print(counter)
