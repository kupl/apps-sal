for _ in range(int(input())):
    n = int(input())
    i = 1
    while True:
        x = pow(2, i - 1) * (pow(2, i) - 1)
        if n < x:
            break
        n -= x
        i += 1
    print(i - 1)
