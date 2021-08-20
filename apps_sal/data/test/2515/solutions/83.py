import bisect


def sieve(n):
    is_prime = [1] * n
    is_prime[0] = 0
    for i in range(2, int(n ** 0.5 // 1 + 2)):
        if is_prime[i - 1]:
            j = i * 2
            while j <= n:
                is_prime[j - 1] = 0
                j += i
    table = [i for i in range(3, n + 1) if is_prime[i - 1] and is_prime[i // 2]]
    return table


q = int(input())
L = sieve(10 ** 5 + 1)
ans = []
for i in range(q):
    (l, r) = map(int, input().split())
    ans.append(bisect.bisect_right(L, r) - bisect.bisect_left(L, l))
print(*ans, sep='\n')
