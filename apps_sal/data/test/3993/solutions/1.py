import sys

n, m, k = list(map(int,sys.stdin.readline().strip().split()))
p = list(map(int,sys.stdin.readline().strip().split()))
i = 0
c = 0
d = 0
while i < m:
    c = c + 1
    d2 = d
    x = k*((p[i]-d2-1)//k) + k
    while p[i]-d2 <= x:
        i = i + 1
        d = d + 1
        if i == m:
            break
print(c)


