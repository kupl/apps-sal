import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
v1 = 0
v2 = 0
p = 0
m = 0
for i in range(0, n):
    if a[i] == 0:
        p = 0
        m = 0
    if a[i] > 0:
        p = p + 1
    if a[i] < 0:
        (p, m) = (m, p)
        m = m + 1
    v1 = v1 + p
    v2 = v2 + m
print(str(v2) + ' ' + str(v1))
