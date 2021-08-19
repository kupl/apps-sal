import math
import collections
t = int(input())
for w in range(t):
    (n, k) = (int(i) for i in input().split())
    l = [int(i) for i in input().split()]
    l1 = [0] * n
    c = 0
    for i in range(n):
        if l[i] > k / 2:
            l1[i] = 1
        elif l[i] < k / 2:
            l1[i] = 0
        elif c % 2 == 0:
            l1[i] = 0
            c += 1
        else:
            l1[i] = 1
            c += 1
    print(*l1)
