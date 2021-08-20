def abc165d_floor_function():
    (a, b, n) = map(int, input().split())
    i = min(n, b - 1)
    max_val = a * i // b - a * (i // b)
    print(max_val)


abc165d_floor_function()
