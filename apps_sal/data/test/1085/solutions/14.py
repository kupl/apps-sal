def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
l = make_divisors(n - 1)
l2 = make_divisors(n)
del l2[0]
ans = len(l) - 1
for i in l2:
    k2 = n
    while True:
        if k2 % i == 1:
            ans += 1
        k2 /= i
        if k2 % 1 != 0:
            break
print(ans)
