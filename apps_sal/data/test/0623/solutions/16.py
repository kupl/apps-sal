a, b = [int(x) for x in input().split()]
count = 0
if a == 1 and b == 1:
    print(0)
else:
    while a > 0 and b > 0:
        if a == 1 or a == 2:
            a += 1
            b -= 2
        elif b == 1 or b == 2:
            b += 1
            a -= 2
        elif a > b:
            a -= 2
            b += 1
        else:
            a += 1
            b -= 2
        count += 1
    print(count)

