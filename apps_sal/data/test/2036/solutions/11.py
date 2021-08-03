from sys import stdin
"""
n=int(stdin.readline().strip())
n,m=map(int,stdin.readline().strip().split())
s=list(map(int,stdin.readline().strip().split()))
"""
n, m, x, y = list(map(int, stdin.readline().strip().split()))
r = [y]
l = [x]
for i in range(1, m + 1):
    if i == y:
        continue
    r.append(i)
for i in range(1, n + 1):
    if i == x:
        continue
    l.append(i)
r1 = r.copy()
r1 = r1[::-1]
x = 0
for i in l:
    if x % 2 == 0:
        for j in r:
            print(i, j)
    else:
        for j in r1:
            print(i, j)
    x += 1
