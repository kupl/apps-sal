for _ in ' ' * int(input()):
    n = int(input())
    ans = len(str(n)) * 9 - 9
    k = 0
    a = int(str(k) * len(str(n)))
    while a <= n:
        a = int(str(k) * len(str(n)))
        if a <= n:
            k += 1
    print(ans + k - 1)
