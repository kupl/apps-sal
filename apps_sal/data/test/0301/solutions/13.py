import sys
readline = sys.stdin.readline

u, v = map(int, readline().split())

if u > v:
    print(-1)
elif (v - u) & 1:
    print(-1)
elif u == v == 0:
    print(0)
elif u == v:
    print(1)
    print(u)
elif u == 0:
    print(2)
    print(v >> 1, v >> 1)
else:
    x = (v - u) >> 1
    if u & x:
        print(3)
        print(u, x, x)
    else:
        print(2)
        print(u | x, x)
