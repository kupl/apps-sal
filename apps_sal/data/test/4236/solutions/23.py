import sys
n, m = map(int, sys.stdin.readline().split())
tab = [False]*m
for loop in range(n):
    d, f = map(int, sys.stdin.readline().split())
    for i in range(d-1, f, 1):
        tab[i] = True
out = list()
r = 0
for loop in range(m):
    if not tab[loop]:
        r+=1
        out.append(loop+1)
print(r)
print(*out)
