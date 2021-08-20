a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c == 0:
    if a != d:
        print(0)
    else:
        print(1)
elif a == 0 or d == 0:
    print(0)
elif a != d:
    print(0)
else:
    print(1)
