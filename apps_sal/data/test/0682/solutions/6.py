# -*- coding: utf-8 -*-
from collections import deque

r1,c1,r2,c2 = map(int, input().split())
if r1 == r2 or c1 == c2:
    n1 = 1
else:
    n1 = 2
   
if (r1+c1)%2 != (r2+c2)%2:
    n2 = 0
elif r1+c1==r2+c2 or r1-c1==r2-c2:
    n2 = 1
else:
    n2 = 2
   
r_min, r_max, c_min, c_max = min(r1, r2), max(r1, r2), min(c1, c2), max(c1, c2)
chess = [[0]*9 for i in range(9)]
q = deque([(r1,c1)])
n3 = 0
while q:
    q2 = deque()
    while q:
        (r, c) = q.popleft()
        if (r, c) == (r2, c2):
            break
        chess[r][c] = 1
        if r-1 >= r_min and c-1 >= c_min and not chess[r-1][c-1]:
            q2.append((r-1, c-1))
        if r-1 >= r_min and not chess[r-1][c]:
            q2.append((r-1, c))
        if r-1 >= r_min and c+1 <= c_max and not chess[r-1][c+1]:
            q2.append((r-1, c+1))
        if c-1 >= c_min and not chess[r][c-1]:
            q2.append((r, c-1))
        if c+1 <= c_max and not chess[r][c+1]:
            q2.append((r, c+1))
        if r+1 <= r_max and c-1 >= c_min and not chess[r+1][c-1]:
            q2.append((r+1, c-1))
        if r+1 <= r_max and not chess[r+1][c]:
            q2.append((r+1, c))
        if r+1 <= r_max and c+1 <= c_max and not chess[r+1][c+1]:
            q2.append((r+1, c+1))
    else:
        q = q2
        n3 += 1
        continue
    break
    
print(n1, n2, n3)
