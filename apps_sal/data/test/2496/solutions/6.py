def gcc(x, y):
    if x == 0: return y
    return gcc(y % x, x)


N = int(input())
A = list(map(int, input().split()))

g = 0

A.sort()

for item in A:
    g = gcc(g, item)

if g != 1:
    print("not coprime")
    return

primes = []

is_prime = [True] * 1100000

is_prime[0] = is_prime[1] = False

for i in range(2, 1100000):
    if not is_prime[i]: continue
    for j in range(i * i, 1100000, i):
        is_prime[j] = False

A_prime = [item for item in A if is_prime[item]]
A_notprime = [item for item in A if not is_prime[item]]

primes = [p for p in range(1100) if is_prime[p]]
used = [False] * 1100000

for item in A_prime:
    used[item] = True

for a in A_notprime:
    for p in primes:
        if a == 1: break
        if a % p != 0: continue

        if used[p]:
            print("setwise coprime")
            # 互いに素でない（共通素因数pで割れる）ペアがAの中にあると，それはsetwise_coprime
            return

        used[p] = True

        while a % p == 0:
            a //= p

    if a > 1:
        if used[a]:
            print("setwise coprime")
            return
        used[a] = True


print("pairwise coprime")
