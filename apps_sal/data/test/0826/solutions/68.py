def __starting_point():
    n = int(input())
    left = 0
    right = 10 ** 18 + 2
    while left < right - 1:
        x = (left + right) // 2
        if x * (x + 1) // 2 <= n + 1:
            left = x
        else:
            right = x
    print(n + 1 - left)


__starting_point()
