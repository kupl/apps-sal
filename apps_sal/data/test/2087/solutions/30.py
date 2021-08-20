def main():
    law = 998244353
    (a, b, c) = list(map(int, input().split()))
    print(sum_mod(a, law) * sum_mod(b, law) * sum_mod(c, law) % law)
    return


def sum_mod(max, law):
    x = max
    y = max + 1
    if x % 2 == 0:
        x //= 2
    else:
        y //= 2
    x = x % law
    y = y % law
    return x * y % law


def __starting_point():
    main()


__starting_point()
