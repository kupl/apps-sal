for _ in range(int(input())):
    n = int(input())
    q = n // 4
    r = n % 4
    a = -1
    if r == 0:
        a = q
    else:
        a = q + 1
    print("9" * (n - a) + "8" * a)
