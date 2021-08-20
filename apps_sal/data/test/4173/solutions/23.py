for _ in range(int(input())):
    (n, a, b) = list(map(int, input().rstrip().split(' ')))
    if a + a > b:
        if n % 2 != 0:
            print(n // 2 * b + a)
        else:
            print(n // 2 * b)
    else:
        print(n * a)
