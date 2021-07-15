from collections import Counter
from itertools import permutations

N, C = list(map(int, input().split()))
D = [list(map(int, input().split())) for i in range(C)]
c = [list([int(s) - 1 for s in input().split()]) for i in range(N)]

d = [Counter(sum([c[j][(i - j) % 3::3] for j in range(N)], []))
     for i in range(3)]
ans = 1000000007
for t in permutations(list(range(C)), 3):
    dis = 0
    for i in range(3):
        for k, v in list(d[i].items()):
            dis += D[k][t[i]] * v
    ans = min(dis, ans)
print(ans)

