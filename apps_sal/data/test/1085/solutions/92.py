N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


a = make_divisors(N)
b = make_divisors(N - 1)
cnt = 0
for i in a:
    if i == 1:
        continue
    k = N
    while k % i == 0:
        k //= i
    if k % i == 1:
        cnt += 1
ans = len(b) - 1 + cnt
print(ans)
