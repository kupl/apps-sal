n = int(input())
if n == 2:
    print(1)
elif n % 2 == 0:
    print(2)
else:
    i = 2
    flag = True
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        i += 1
    if flag:
        print(1)
    else:
        i = 2
        flag = True
        while i * i <= n - 2:
            if (n - 2) % i == 0:
                flag = False
                break
            i += 1
        if flag:
            print(2)
        else:
            print(3)
