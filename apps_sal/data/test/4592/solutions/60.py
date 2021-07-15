import math
url = "https://atcoder.jp//contests/abc052/tasks/arc067_a"


def get_list_eratosthenes(n):
    if n < 2:
        return [0]*(n+1)
    prime = [1]*(n+1)
    prime[0] = prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not prime[i]: continue
        for j in range(i * 2, n + 1, i):
            prime[j] = 0
    return prime


def main():
    N = int(input())
    tmp = N
    primes = get_list_eratosthenes(N)
    ans = 1
    for p in range(2, N+1):
        if primes[p] == 0: continue
        cur = p
        num = 0
        while cur <= N:
            num += N // cur
            cur *= p
        ans *= (num + 1)
        ans %= 10**9+7
    print(ans)



def __starting_point():
    main()

__starting_point()
