import math

w, m = list(map(int, input().split()))
if w == 2:
    print("YES")
else:
    n = math.ceil(math.log(1e9, w))
    for mask in range(1 << n):
        s = m
        p = 1
        for i in range(n):
            if mask & (1 << i):
                s += p
            p *= w
        while s > 0:
            if s % w > 1:
                break
            s //= w
        else:
            print("YES")
            break
    else:
        print("NO")

