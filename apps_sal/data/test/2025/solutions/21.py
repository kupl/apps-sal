n = int(input())
for i in range(n):
    a = int(input())
    if a % 4 == 0:
        print(a // 4)
    elif a % 2 == 1:
        if a < 9:
            print(-1)
        elif a == 9:
            print(1)
        else:
            a = a - 9
            x = a % 4
            k = 3
            while x < a:
                x += 4
                k = 0
                for i in range(2, int(x ** 0.5 + 1)):
                    if x % i == 0:
                        k = 1
                        break
                if k == 1:
                    print((a - x) // 4 + 2)
                    k = 2
                    break
            if x > a or k == 3 or k == 0:
                print(-1)
            elif x == a and k != 2:
                print(2)
    else:
        x = a % 4
        k = 3
        while x < a:
            x += 4
            k = 0
            for i in range(2, int(x ** 0.5 + 1)):
                if x % i == 0:
                    k = 1
                    break
            if k == 1:
                print((a - x) // 4 + 1)
                k = 2
                break
        if x > a or k == 3 or k == 0:
            print(-1)
        elif x == a and k != 2:
            print(1)
