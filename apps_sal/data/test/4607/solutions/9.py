def resolve():
    a, b = map(int, input().split())
    if a <= b: c = a
    else: c = a - 1
    print(c)


resolve()
