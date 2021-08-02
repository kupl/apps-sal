t = int(input())
while t:
    t -= 1
    n = int(input())
    a = input()
    if n % 2 == 0:
        flag = 0
        for i in range(1, n, 2):
            if int(a[i]) % 2 == 0:
                flag += 1
                break
        if flag:
            print(2)
        else:
            print(1)
    else:
        flag = 0
        for i in range(0, n, 2):
            if int(a[i]) % 2 == 1:
                flag += 1
                break
        if flag:
            print(1)
        else:
            print(2)
