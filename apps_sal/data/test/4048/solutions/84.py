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


N = int(input())
A = make_divisors(N)
ans = pow(10, 15)
for x in A:
    temp = N // x + x
    ans = min(ans, temp)
print(ans - 2)
