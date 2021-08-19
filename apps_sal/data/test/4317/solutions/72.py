def resolve():
    (a, b) = map(int, input().split())
    print(max(a + b, a - b, a * b))


resolve()
