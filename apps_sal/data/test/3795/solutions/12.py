source = input
amount = int(source())
price_dollar = int(source())
price_euro = int(source())


def get_answer(amount, p1, p2):
    best = amount
    for other in range(p1):
        a1 = amount - other * p2
        if a1 == 0:
            return 0
        if a1 < 0:
            break
        change = a1 % p1
        best = min(change, best)
    return best


print(get_answer(amount, price_dollar, price_euro * 5))
