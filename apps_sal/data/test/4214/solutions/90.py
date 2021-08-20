import math
import itertools
n = int(input())
X = list((list(map(int, input().split())) for _ in range(n)))
L = list(itertools.permutations(range(n), n))
ans = 0
for l in L:
    dist = 0
    for i in range(n - 1):
        (s, t) = (l[i], l[i + 1])
        vx = X[s][0] - X[t][0]
        vy = X[s][1] - X[t][1]
        dist += math.sqrt(vx ** 2 + vy ** 2)
    ans += dist
print(ans / len(L))
