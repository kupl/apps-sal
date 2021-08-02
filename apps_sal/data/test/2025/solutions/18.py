n = int(input())
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        if a < 4:
            print(-1)
        else:
            print(a // 4)
    else:
        if a < 9:
            print(-1)
        else:
            if a - 9 < 4 and a - 9 > 0:
                print(-1)
            else:
                print(1 + (a - 9) // 4)
