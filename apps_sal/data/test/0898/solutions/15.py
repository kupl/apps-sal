def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


n, m = list(map(int, input().split()))

if n % m == 0:
    print((int(n / m)))
    return
else:
    lst = make_divisors(m)[::-1]
    for i in lst:
        if i == 1:
            print(i)
            return
        if m - i * (n - 1) > 0:
            if (m - i * (n - 1)) % i == 0:
                print(i)
                return
        else:
            continue
