def user99():
    n = int(input())
    nn = n

    N = 10**6
    prime = [True] * N
    prime[0] = prime[1] = False;

    for i in range(2, N, 1):
        if i * i > N: break
        if prime[i]:
            for j in range(i * i, N, i):
                prime[j] = False

    primes = []
    for i in range(N):
        if prime[i]:
            primes.append(i)

    b = []
    for p in primes:
        if n % p != 0: continue
        power = 0
        while n % p == 0:
            n //= p
            power += 1
        b.append([p, power])

    steps, x = 0, 1

    max_power = 0
    for i in b:
        max_power = max(max_power, i[1])
        x *= i[0]

    for i in range(10):
        if max_power <= 2**i:
            max_power = 2**i
            steps = i
            break

    if x**(2**steps) != nn:
        steps += 1

    print(x, steps)


user99()
