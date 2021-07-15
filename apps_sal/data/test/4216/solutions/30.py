def get_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            upper_divisors.append(n//i)
        i += 1
    return [lower_divisors, upper_divisors]

n = int(input())

up = get_divisors(n)[0]
dn = get_divisors(n)[1]

ans = 11
for a, b in zip(up, dn):
    a = str(a)
    b = str(b)
    f = max(len(a), len(b))
    ans = min(ans, f)

print(ans)
