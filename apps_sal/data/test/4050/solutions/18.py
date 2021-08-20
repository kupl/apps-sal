from collections import defaultdict
from itertools import accumulate
N = int(input())
H = defaultdict(lambda: [])
A = list(map(int, input().split()))
AA = [0] + list(accumulate(A))
for i in range(1, N + 1):
    for j in range(i):
        H[AA[i] - AA[j]].append((i, j))
ctr = 0
ans = []
for L in list(H.values()):
    if ctr >= len(L):
        continue
    L.sort()
    ansc = []
    pi = -1
    for (i, j) in L:
        if j >= pi:
            ansc.append((j + 1, i))
            pi = i
    if ctr < len(ansc):
        ans = ansc.copy()
        ctr = len(ans)
print(ctr)
for (j, i) in ans:
    print(j, i)
