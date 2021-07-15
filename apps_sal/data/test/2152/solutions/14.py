def __starting_point():
    n = int(input())
    prices = []
    needs = []

    for i in range(n):
        n, p = map(int, input().split())
        prices.append(p)
        needs.append(n)

    total = 0
    curr = needs[0]
    curr_p = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < curr_p:
            total += curr_p * curr
            curr = 0
            curr_p = prices[i]

        curr += needs[i]

    total += curr_p * curr

    print(total)
__starting_point()
