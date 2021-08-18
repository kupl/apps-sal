def factorize(n):
    result = []
    N = n
    i = 2
    while i * i <= N:
        if n % i == 0:
            power = 0
            while n % i == 0:
                n = n // i
                power += 1
            result.append((i, power))
        i += 1
    if n != 1:
        result.append((n, 1))
    return result


n, b = input().split()
n = int(n)
b = int(b)
p = factorize(b)

ans = None
for (prime, power) in p:
    k = prime
    pp = 0
    while k <= n:
        pp += n // k
        k *= prime
    res = pp // power
    if ans == None or ans > res:
        ans = res

print(ans)
