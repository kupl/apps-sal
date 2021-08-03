import sys
import math

n = int(sys.stdin.readline())

d = dict()
for i in range(n):
    x, k = [int(x) for x in (sys.stdin.readline()).split()]
    if k in d:
        t = d[k]
        if x not in t[1]:
            if(x - 1 == t[0]):
                t[0] = x
                t[1].add(x)
            else:
                print("NO")
                return
    else:
        if(x > 0):
            print("NO")
            return

        d[k] = [x, {x}]

print("YES")
