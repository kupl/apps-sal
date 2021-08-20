import itertools
import math
n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
q = list(itertools.permutations(range(n)))
m = len(q)
k_sum = 0
for i in range(m):
    for j in range(n - 1):
        a = xy[q[i][j]][0] - xy[q[i][j + 1]][0]
        x = a ** 2
        b = xy[q[i][j]][1] - xy[q[i][j + 1]][1]
        y = b ** 2
        k_sum += math.sqrt(x + y)
print(k_sum / m)
