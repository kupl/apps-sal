import sys

u, v = list(map(int, sys.stdin.readline().strip().split()))
w = v - u
if w % 2 == 1 or w < 0:
    print(-1)
elif w == 0:
    if u == 0:
        print(0)
    else:
        print(1)
        print(str(u))
else:
    w = w // 2
    if u & w == 0:
        print(2)
        print(str(u + w) + " " + str(w))
    else:
        print(3)
        print(str(u) + " " + str(w) + " " + str(w))
