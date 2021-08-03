for _ in [0] * int(input()):
    k, x = list(map(int, input().split()))
    print(x + (k - 1) * 9)
