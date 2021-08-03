def __starting_point():
    n, a, b = list(map(int, input().split()))
    prices = [a, b]
    colors = list(map(int, input().split()))
    result = 0
    for i in range(n // 2):
        j = n - 1 - i
        if colors[i] != colors[j] and colors[i] != 2 and colors[j] != 2:
            print(-1)
            return
        if colors[i] == colors[j] == 2:
            result += 2 * min(prices)
        elif colors[i] == 2:
            result += prices[colors[j]]
        elif colors[j] == 2:
            result += prices[colors[i]]
    if n & 1 and colors[n // 2] == 2:
        result += min(prices)
    print(result)


__starting_point()
