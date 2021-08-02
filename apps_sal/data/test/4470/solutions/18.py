n = int(input())
for i in range(n):
    x = int(input())
    k = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            k += 1
        elif x % 3 == 0:
            x = x - x // 3
            k += 1
        elif x % 5 == 0:
            x = x - x // 5
            k += 1
        else:
            k = -1
            break
    print(k)
