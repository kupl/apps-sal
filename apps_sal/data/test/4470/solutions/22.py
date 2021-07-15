for i in range(int(input())):
    x = int(input())
    k = 0
    fl = True
    while fl:
        fl = x % 2 == 0 or x % 3 == 0 or x % 5 == 0
        if fl:
            if x % 2 == 0:
                while x % 2 == 0:
                    x //= 2
                    k += 1
            elif x % 3 == 0:
                x *= 2
                x //= 3
                k += 1
            elif x % 5 == 0:
                x *= 4
                x //= 5
                k += 1
    if x != 1:
        print(-1)
    else:
        print(k)
                

