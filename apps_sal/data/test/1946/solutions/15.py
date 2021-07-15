from collections import defaultdict as dd, deque

E = set()

n = int(input())
C1 = dd(int)
for _ in range(n):
    i,c = list(map(int,input().split()))
    C1[i] = c
    E.add(i)

m = int(input())
C2 = dd(int)
for _ in range(m):
    i,c = list(map(int,input().split()))
    C2[i] = c
    E.add(i)

e = 0
for el in E:
    e += max(C1[el],C2[el])
print(e)

