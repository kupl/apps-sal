n = int(input())
for i in range(n):
    a = int(input())
    if a % 4 == 0:
        print(a // 4)
    elif a % 4 == 2:
        a -= 6
        if a < 0:
            print(-1)
        else:
            print(a // 4 + 1)
    elif a % 4 == 1:
        a -= 9
        if a < 0:
            print(-1)
        else:
            print(a // 4 + 1)
    else:
        a -= 15
        if a < 0:
            print(-1)
        else:
            print(a // 4 + 2)
