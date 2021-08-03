for i in range(int(input())):
    n, a, b = map(int, input().split())
    best = min(a * 2, b)
    print(n // 2 * best + n % 2 * a)
