def arc104_a():
    a, b = (int(x) for x in input().split())
    x = (a + b) // 2
    y = (a - b) // 2
    print(f"{x} {y}")

arc104_a()
