def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


n, m = map(int, input().split())
h = m // n
ans = 0

for d in make_divisors(m):
    if d <= h:
        ans = max(ans, d)

print(ans)
