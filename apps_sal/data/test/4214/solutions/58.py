import math
import itertools

n = int(input())
pos = []
for i in range(n):
    x, y = map(int, input().split())
    pos.append([x, y])

iter = list(itertools.permutations(list(range(n))))
total = 0
for i in iter:
    for j in range(n - 1):
        p1 = pos[i[j]]
        p2 = pos[i[j + 1]]
        d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        total += d
print(total / len(iter))
