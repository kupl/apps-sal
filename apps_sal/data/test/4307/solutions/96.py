N = int(input())


def make_divisor(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


cnt = 0
for i in range(1, N + 1):
    if len(make_divisor(i)) == 8 and i % 2 == 1:
        cnt += 1
print(cnt)
