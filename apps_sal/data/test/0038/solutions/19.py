from collections import deque

n, L = list(map(int, input().split()))
d1 = [int(i) for i in input().split()]
d2 = deque([int(i) for i in input().split()])
ans = False
if n == 1:
    ans = True

for i in range(n):
    if ans:
        break
    diff = (d1[0]-d2[0])%L
    fl = True
    for j in range(n):
        if (d1[j]-d2[j])%L != diff:
            fl = False
    if fl:
        ans = True
    d2.rotate(1)

print(["NO","YES"][ans])

