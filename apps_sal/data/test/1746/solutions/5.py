import sys
sys.setrecursionlimit(10 ** 5)
n = int(input())
g = [[] for i in range(n)]
for i in range(1, n):
    z = int(input()) - 1
    g[z].append(i)
# print(g)
b = True
for el in g:
    if len(el) == 0:
        continue
    z = 0
    for v in el:
        z += len(g[v]) == 0
    if z <= 2:
        b = False
if b:
    print("Yes")
else:
    print("No")
