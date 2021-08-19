from math import *
mod = 1000000007
for zz in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    a = set(a)
    v = 1
    while True:
        if v in a:
            pass
        else:
            if x <= 0:
                v -= 1
                break
            x -= 1
        v += 1
    print(v)
