def make_divisors(n: int) -> list:
    divisors = []
    for k in range(1, int(n ** 0.5) + 1):
        if n % k == 0:
            divisors.append(k)
            if k != n // k:
                divisors.append(n // k)
    divisors = sorted(divisors)
    return divisors


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    divs = make_divisors(n)
    ans = 10 ** 18
    for div in divs:
        if div <= k:
            ans = min(ans, n // div)
    print(ans)
