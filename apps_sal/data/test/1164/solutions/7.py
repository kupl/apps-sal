import decimal
import itertools


def is_digit_or_dot(char):
    return char.isdigit() or char == '.'


def compute(bill):
    prices = []
    for (k, v) in itertools.groupby(bill, is_digit_or_dot):
        if not k:
            continue
        segments = ''.join(v).split('.')
        if len(segments[-1]) == 2:
            cent = decimal.Decimal('.' + segments[-1])
            dollar = decimal.Decimal(''.join(segments[:-1]))
            price = cent + dollar
        else:
            price = decimal.Decimal(''.join(segments))
        prices.append(price)
    amount = sum(prices)
    (dollar, cent) = divmod(amount, 1)
    ans = '{:,d}'.format(int(dollar)).replace(',', '.')
    if cent > 0:
        ans += str(cent)[1:]
    return ans


def main():
    print(compute(input()))


def __starting_point():
    main()


__starting_point()
