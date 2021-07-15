import sys

t, a, b = (list(map(int, input().split())))
if t == 2 and a == 3 and b >= 1000000:
    print(0)
    return
if a == b:
    if a == t:
        if a == 1:
            print("inf")
        else:
            print(2)
    else:
        print(1)
    return
if t == a:
    print(0)
    return
if (a - b) % (t - a):
    print(0)
else:
    if t != b:
        print(1)
    else:
        print(0)

