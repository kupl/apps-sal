q = int(input())
for i in range(q):
    a = int(input())
    if a % 2:
        if a == 9:
            print(1)
        elif a - 9 > 2:
            print((a - 9) // 4 + 1)
        else:
            print(-1)
    elif a > 2:
        print(a // 4)
    else:
        print(-1)
