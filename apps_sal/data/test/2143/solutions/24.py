from sys import setrecursionlimit
setrecursionlimit(10**6) 
inn = lambda: input().strip()
mapp = lambda: map(int, inn().split(" "))

N = int(inn())
C = list(mapp())
C.sort()

from collections import defaultdict
summ = defaultdict(int)

for a in range(N):
    for b in range(a+1,N):
        summ[C[a]+C[b]] += 1

answer = 0
for key in summ:
    answer = max(answer, summ[key])

print(answer)
