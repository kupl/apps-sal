a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (b - c) >= 0:
    print("delicious")
else:
    if (b - c) >= -a:
        print("safe")
    else:
        print("dangerous")
