from itertools import groupby
n, k = [int(x) for x in input().split()]

size = sorted([int(x) for x in input().split()])

size = [(k, len(list(l))) for k, l in groupby(size)]

res = size[-1][-1]
for i in range(len(size) - 1):
    if size[i + 1][0] > size[i][0] + k:
        res += size[i][1]

print(res)
