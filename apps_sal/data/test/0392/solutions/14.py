def __starting_point():
    n = int(input())
    total = 1
    for i in range(2, int(pow(n, 0.5)) + 2):
        if n % i == 0:
            total *= i

        while n % i == 0:
            n //= i

    print(total * n)


__starting_point()
