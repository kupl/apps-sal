def main():
    buf = input()
    n = int(buf)
    prime_map = dict()
    a = []
    for i in range(2, n + 1):
        first_prime = first_prime_factor(i)
        if first_prime not in prime_map:
            prime_map[first_prime] = len(prime_map) + 1
        a.append(prime_map[first_prime])
    print(' '.join(list(map(str, a))))


def first_prime_factor(x):
    n = x
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return x


def __starting_point():
    main()


__starting_point()
