def christmas_eve_eve(price_list: list):
    price_list.sort()
    price_list[-1] /= 2
    return int(sum(price_list))


def __starting_point():
    prices = []
    n = int(input())
    for i in range(n):
        prices.append(int(input()))
    print(christmas_eve_eve(prices))


__starting_point()
