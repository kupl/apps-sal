nearest_prime = [0] * 100004


def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for (index, i) in enumerate(primes):
        if i == True:
            for j in range(index * index, n + 1, index):
                primes[j] = False
    return primes


def sub_from_nearest(a):
    return nearest_prime[a] - a


def main():
    (m, n) = [int(x) for x in input().split()]
    prime_bool = sieve(100003)
    nearest = -1
    for (i, bool) in list(enumerate(prime_bool))[::-1]:
        if bool:
            nearest = i
            nearest_prime[i] = i
        else:
            nearest_prime[i] = nearest
    matrix = []
    for i in range(0, m):
        lis = [sub_from_nearest(int(x)) for x in input().split()]
        matrix.append(lis)
    min = 10000000
    for i in matrix:
        su = sum(i)
        if su < min:
            min = su
    for i in range(0, n):
        su = sum([row[i] for row in matrix])
        if su < min:
            min = su
    print(min)


def __starting_point():
    main()


__starting_point()
