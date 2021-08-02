#Python is love <3
a = int(input())
b = int(input())
if((abs(b - a)) % 2 == 0):
    w = (abs(b - a)) // 2
    p = (w * (w + 1))
    print(p)
else:
    w = (abs(b - a)) // 2
    p = (w * (w + 1))
    print(p + w + 1)
