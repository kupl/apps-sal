nmax = 1000010
primes = [0 for i in range(nmax)]


def get_primes():
    nonlocal primes

    n = 2
    while n < nmax:
        num = 2 * n
        while num < nmax:
            primes[num] = n
            num += n
        num = n + 1
        while num < nmax and primes[num] != 0:
            num += 1
        n = num


def algo(x2):
    nonlocal primes

    p2 = primes[x2]
    min_x1 = x2 - p2 + 1
    min_x0 = nmax

    for x1 in range(min_x1, x2 + 1):
        p1 = primes[x1]
        x0 = x1 - p1 + 1

        if x0 < min_x0:
            min_x0 = x0
            # print("p1 is ", p1, " for ", x0)
    return min_x0


x2 = int(input().strip())
get_primes()
print(algo(x2))
