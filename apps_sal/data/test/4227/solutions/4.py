from itertools import permutations
from math import factorial

n, m = map(int, input().split(' '))
edge = []
for i in range(m):
    ai, bi = map(int, input().split(' '))
    edge.append([ai, bi])

l = [i for i in range(1, n + 1)]
ls = list(permutations(l))
ans = 0
for i in range(factorial(n - 1)):
    y = 0
    for j in range(n - 1):
        for k in edge:
            if (ls[i][j + 1] in k) and (ls[i][j] in k):
                y += 1
    if y == n - 1:
        ans += 1

print(ans)
