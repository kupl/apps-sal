def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


N = int(input())
ans = len(make_divisors(N - 1)) - 1
for i in make_divisors(N):
    if i == 1:
        continue
    Ni = int(N / i)
    while Ni % i == 0:
        Ni = int(Ni / i)
    if Ni % i == 1:
        ans += 1
print(ans)
