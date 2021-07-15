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

N = int(input())
divsN = make_divisors(N)
divsN2 = make_divisors(N-1)
divsN.pop(0)

ans = len(divsN2)-1

for div in divsN:
    n = N+1-1
    while True:
        if n%div != 0 or n==1:
            break
        n //= div
    if n%div == 1:
        ans += 1

print(ans)
