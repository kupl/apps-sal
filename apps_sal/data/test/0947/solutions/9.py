for _ in range(int(input())):
    n = int(input())
    if n > 3:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        if n % i == 0:
            print(n // i, n - n // i)
        else:
            print(1, n - 1)
    else:
        print(1, n - 1)
