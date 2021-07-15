from itertools import permutations
from math import factorial

n, m = list(map(int, input().split(' ')))
edge = []

for i in range(m):
    ai, bi = list(map(int, input().split(' ')))
    edge.append([ai,bi])


x = [i for i in range(1,n+1)]
ls = list(permutations(x))
ans = 0
for l in range(factorial(n-1)):
    cnt = 0
    for i in range(n-1):
        for j in range(m):
            if (ls[l][i] in edge[j]) and (ls[l][i+1] in edge[j]):
                cnt += 1
    if cnt == n-1:
        ans += 1


print(ans)

