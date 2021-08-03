def abc165d_floor_function():
    a, b, n = map(int, input().split())
    i = min(n, b - 1)
    max_val = a * i // b - a * (i // b)
    # for i in range(1, n+1):
    #     v = a*i//b - a*(i//b)
    #     max_val = max(max_val, v)
    print(max_val)


abc165d_floor_function()
