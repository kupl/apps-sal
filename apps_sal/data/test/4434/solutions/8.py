for _ in range(int(input())):
    n = int(input())
    print(sum((i * ((2 * i + 1) ** 2 - (2 * (i - 1) + 1) ** 2) for i in range(1, n // 2 + 1))))
