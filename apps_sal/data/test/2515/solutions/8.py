from itertools import accumulate

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


like_numbers = [0] * (10 ** 6)
for p in primes(10 ** 5):
    like_numbers[p * 2 - 1] += 1
    like_numbers[p] += 1

like_numbers = [1 if i == 2 else 0 for i in like_numbers]
like_numbers = list(accumulate(like_numbers))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(like_numbers[r] - like_numbers[l-1])
