a = int(input())
b = 0
if a == 2:
    print(4)
elif a == 1:
    print(4)
else:
    while a != 4:
        if a % 2 == 0:
            a = a // 2
            b = b + 1
        else:
            a = 3 * a + 1
            b = b + 1
    print(b + 4)
