def main():
    buf = input()
    n = int(buf)
    op_count = 0
    factor = prime_factorization(n)
    c_max = 1
    first_c = None
    all_same = True
    min_number = 1
    for (f, c) in list(factor.items()):
        if c > c_max:
            c_max = c
        if first_c == None:
            first_c = c
        elif c != first_c:
            all_same = False
        min_number *= f
    if check_power_of_2(c_max) and all_same:
        pass
    else:
        op_count += 1
    if not check_power_of_2(c_max):
        c_max = c_max << 1
        c_max = c_max & c_max - 1
    while c_max > 1:
        c_max //= 2
        op_count += 1
    print(min_number, op_count)


def check_power_of_2(x):
    return x != 0 and x & x - 1 == 0


def prime_factorization(number):
    n = number
    i = 2
    factor = {}
    while i * i <= n:
        while n % i == 0:
            if i in factor:
                factor[i] += 1
            else:
                factor.update({i: 1})
            n //= i
        i += 1
    if n > 1 or not factor:
        if n in factor:
            factor[n] += 1
        else:
            factor.update({n: 1})
    return factor


def __starting_point():
    main()


__starting_point()
