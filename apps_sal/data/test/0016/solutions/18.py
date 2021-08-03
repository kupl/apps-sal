a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and d == 0:
    if c == 0:
        print(1)
    else:
        print(0)
else:
    if a == d:
        print(1)
    else:
        print(0)
