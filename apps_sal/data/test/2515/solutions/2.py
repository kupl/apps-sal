def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


primes = set(get_sieve_of_eratosthenes(10**5))

cumsum = [0]
for i in range(1, 10**5 + 1):
    if i % 2 == 1 and i in primes and (i + 1) // 2 in primes:
        cumsum.append(cumsum[-1] + 1)
    else:
        cumsum.append(cumsum[-1])

Q = int(input())
for i in range(Q):
    l, r = list(map(int, input().split()))
    ans = cumsum[r] - cumsum[l - 1]
    print(ans)
