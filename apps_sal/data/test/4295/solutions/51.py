def resolve():
    n, k = map(int, input().split())
    print(min(n - k * (n // k), abs(n - k * (n // k) - k)))


resolve()
