MOD = int(1000000000.0 + 7)


def log_power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base % MOD
    if exp % 2 == 1:
        return base * log_power(base, exp - 1) % MOD
    root = log_power(base, exp // 2)
    return root * root % MOD


def total(fact, limit):
    prod = 1
    power = fact
    while power <= limit:
        prod = prod * log_power(fact, limit // power) % MOD
        prod %= MOD
        power *= fact
    return prod


def solve(num, limit):
    fact = 2
    prod = 1
    while fact * fact <= num:
        count = 0
        while num % fact == 0:
            num //= fact
            count += 1
        if count > 0:
            prod = prod * total(fact, limit) % MOD
        fact += 1
    if num > 1:
        prod = prod * total(num, limit) % MOD
    return prod


def __starting_point():
    (num, limit) = list(map(int, input().split()))
    print(solve(num, limit))


__starting_point()
