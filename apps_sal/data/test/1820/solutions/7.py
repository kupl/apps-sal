import math
t = int(input())
for w in range(t):
    n = int(input())
    l = sorted([int(i) for i in input().split()])
    if l[0] + l[1] > l[-1]:
        print(-1)
    else:
        print(1, 2, n)
