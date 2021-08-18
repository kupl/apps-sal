def brute(n):

    sol = 0

    for x in range(1, n + 1):

        valid = 1

        for j in range(2, 11):
            if x % j == 0:
                valid = 0

        sol += valid

    return sol


N = int(input())

sol = 0
primes = [2, 3, 5, 7]

for state in range(1, 2 ** len(primes)):

    numbBits = 0
    prod = 1

    for j in range(len(primes)):
        if (1 << j) & state:
            numbBits += 1
            prod *= primes[j]

    if numbBits % 2 == 1:
        sol += N // prod
    else:
        sol -= N // prod

print(N - sol)
