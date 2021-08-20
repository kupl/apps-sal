def __starting_point():
    n = int(input())
    for i in range(n):
        n = int(input())
        k = 4
        while True:
            if n % (k - 1) == 0:
                print(n // (k - 1))
                break
            else:
                k *= 2


__starting_point()
