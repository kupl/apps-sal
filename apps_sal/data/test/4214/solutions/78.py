import itertools
import math
N = int(input())
ls, val = [], 0
perm = itertools.permutations(range(N))
for i in range(N):
    x, y = map(int, input().split(' '))
    ls.append([x, y])
for i in perm:
    for j in range(N - 1):
        val += math.sqrt((ls[i[j + 1]][0] - ls[i[j]][0]) ** 2 + (ls[i[j + 1]][1] - ls[i[j]][1]) ** 2)
print(val / math.factorial(N))
