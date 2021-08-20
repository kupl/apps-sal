import math
t = int(input())
for g in range(t):
    (l, r) = list(map(int, input().split()))
    if r < 2 * l:
        print('-1', '-1')
    else:
        print(l, 2 * l)
