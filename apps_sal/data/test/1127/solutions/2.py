tests = int(input())
for test in range(tests):
    n = int(input())
    a = [int(i) for i in input()]
    if n % 2 == 0:
        f = False
        for i in range(1, n, 2):
            if a[i] % 2 == 0:
                f = True
                break
        if f:
            print(2)
        else:
            print(1)
    else:
        f = False
        for i in range(0, n, 2):
            if a[i] % 2 == 1:
                f = True
                break
        if f:
            print(1)
        else:
            print(2)
        

