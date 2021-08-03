for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if b > 2 * a:
        print(n * a)
    else:
        print((n // 2) * b + (n % 2) * a)
