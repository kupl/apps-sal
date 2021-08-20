(n, m) = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors


numbers = make_divisors(m)
for i in range(len(numbers)):
    if numbers[i] <= m / n:
        print(numbers[i])
        break
