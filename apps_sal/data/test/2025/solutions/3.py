n = int(input())
for i in range(n):
    a = int(input())

    if a % 4 == 0:
        print(a // 4)
    elif (a - 6) >= 0 and (a - 6) % 4 == 0:
        print(((a - 6) // 4) + 1)
    elif (a - 9) >= 0 and (a - 9) % 4 == 0:
        print(((a - 9) // 4) + 1)
    elif (a - 15) >= 0 and (a - 15) % 4 == 0:
        print(((a - 15) // 4) + 2)
    else:
        print(-1)

