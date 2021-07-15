import itertools
from collections import deque

N,M = map(int,input().split())
table = [[0]*N for _ in range(N)]
ans = 0
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    table[a][b] = 1
    table[b][a] = 1

p = [i for i in range(1,N)]
q = list(itertools.permutations(p))

s = deque()
for i in range(len(q)):
    x = 0
    flag = 0
    for y in q[i]:
        if table[x][y] == 0:
            flag = 1
            break
        x = y
    if flag == 0:
        ans += 1

print(ans)
