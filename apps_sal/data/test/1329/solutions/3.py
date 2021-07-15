from collections import Counter
def prime_factorize(n):
    i = 2
    factors = []
    while i*i <= n:
        while n%i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)

n = int(input())

c = Counter([])
for i in range(1, n+1):
    c += prime_factorize(i)

def f(x):
    return len([i for i,cnt in c.items() if cnt >= x-1])

ans = 0
ans += f(5) * (f(5) - 1) // 2 * (f(3) - 2)
ans += f(5*5) * (f(3) - 1)
ans += f(3*5) * (f(5) - 1)
ans += f(3*5*5)

print(ans)
