def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


N = int(input())
N_div = make_divisors(N)[1:]
N1_div = make_divisors(N - 1)[1:]

ans = len(N1_div)

for i in N_div:
    n = N
    while n % i == 0:
        n //= i
    if n % i == 1:
        ans += 1
print(ans)
