x, y = map(int, input().split())
a = [4, 6, 9, 11]
b = 0
c = 0
if x == 2 or y == 2:
    print("No")
else:
    if x in a:
        b = 1
    if y in a:
        c = 1
    if (b + c) % 2 == 0:
        print("Yes")
    else:
        print("No")
