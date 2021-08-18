mod_number = 10 ** 9 + 7


def power_mod(n, p):
    if p < 2:
        return (n ** p) % mod_number
    sub_result = power_mod(n, p // 2)
    if p % 2 == 0:
        return (sub_result ** 2) % mod_number
    else:
        return (sub_result ** 2 * n) % mod_number


def get_frequency_map(items):
    frequency_map = {}
    for item in items:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1

    return frequency_map


def get_product_of_others(items):
    length = len(items)

    prefix_product_of_others = [1] * length
    suffix_product_of_others = [1] * length
    for i in range(1, length):
        prefix_product_of_others[i] = (prefix_product_of_others[i - 1] * items[i - 1]) % (mod_number - 1)

    for i in reversed(list(range(length - 1))):
        suffix_product_of_others[i] = (suffix_product_of_others[i + 1] * items[i + 1]) % (mod_number - 1)

    return [prefix_product_of_others[i] * suffix_product_of_others[i]
            for i in range(length)]


def main():
    m = int(input())
    prime_factors = [int(t) for t in input().split()]

    prime_factors_count_map = get_frequency_map(prime_factors)
    ordered_prime_factors = list(prime_factors_count_map.keys())

    each_prime_factor_choices = [prime_factors_count_map[prime_factor] + 1 for prime_factor in ordered_prime_factors]

    other_prime_factors_choices = get_product_of_others(each_prime_factor_choices)

    total_factors = 1
    for i, prime_factor in enumerate(ordered_prime_factors):
        prime_factor_count = prime_factors_count_map[prime_factor]
        total_power_of_factor = ((prime_factor_count * (prime_factor_count + 1)) // 2)
        product_of_factor_by_prime_factor = power_mod(prime_factor, total_power_of_factor % (mod_number - 1))
        total_factors *= power_mod(product_of_factor_by_prime_factor, other_prime_factors_choices[i] % (mod_number - 1))

    print(total_factors % mod_number)


def __starting_point():
    main()


__starting_point()
