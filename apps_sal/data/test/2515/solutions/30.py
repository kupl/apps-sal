import bisect
q = int(input())


def sieve(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False

    for i in range(2, int((n**0.5) // 1 + 2)):
        if is_prime[i - 1]:
            j = 2 * i
            while j <= n:
                is_prime[j - 1] = False
                j += i
    table = [i for i in range(1, n + 1) if is_prime[i - 1] and is_prime[i // 2]]
    return table[1:]


x = sieve(10**5 + 1)
ans = []

for _ in range(q):
    l, r = map(int, input().split())
    ans.append(bisect.bisect_right(x, r) - bisect.bisect_left(x, l))

print(*ans, sep="\n")
