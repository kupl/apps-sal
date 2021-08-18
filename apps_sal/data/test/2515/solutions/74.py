def cal_primes(N):
    candidate = [*range(2, N + 1)]
    primes = []

    while candidate[0]**2 <= N:
        primes.append(candidate[0])
        candidate = [*filter(lambda x: x % candidate[0] != 0, candidate)]

    primes.extend(candidate)
    return primes


Q = int(input())
primes = set(cal_primes(10**5))
res = [0] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    if i % 2 == 1 and i in primes and (i + 1) // 2 in primes:
        res[i] = res[i - 1] + 1
    else:
        res[i] = res[i - 1]
for i in range(Q):
    l, r = map(int, input().split())
    print(res[r] - res[l - 1])
