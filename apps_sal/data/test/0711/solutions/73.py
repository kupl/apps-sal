MOD = 10 ** 9 + 7
(N, M) = map(int, input().split())
primes = [0]
while M % 2 == 0:
    primes[0] += 1
    M //= 2
if M != 1:
    for i in range(3, int(M ** 0.5 + 1), 2):
        if M % i == 0:
            primes.append(0)
            while M % i == 0:
                primes[-1] += 1
                M //= i
            if M == 1:
                break
    else:
        primes.append(1)
combinations = [1]
p_max = max(primes)
for p in range(1, p_max + 1):
    combinations.append(combinations[-1] * (p + N - 1) * pow(p, MOD - 2, MOD) % MOD)
ans = 1
for p in primes:
    ans *= combinations[p]
    ans %= MOD
print(ans)
