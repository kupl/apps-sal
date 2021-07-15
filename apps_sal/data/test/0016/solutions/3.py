a = int(input())
b = int(input())
c = int(input())
d = int(input())

f = True
k = 2 * a
if c:
    if k < 1:
        print(0)
    else:
        if k == 2 * d:
            print(1)
        else:
            print(0)
else:
    if k == 2 * d:
        print(1)
    else:
        print(0)

