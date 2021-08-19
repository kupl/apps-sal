import math
n = int(input())
l = list(map(int, input().split()))
l.sort()
if l.count(l[0]) != 2 * n:
    for x in l:
        print(x, end=' ')
    print()
else:
    print(-1)


# python3 c.py
