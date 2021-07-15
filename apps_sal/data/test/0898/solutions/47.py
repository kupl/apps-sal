def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N, M = list(map(int, input().split()))

divisors = make_divisors(M)
ans = 0
for d in divisors:
    if N*d <= M:
        ans = d

print(ans)


