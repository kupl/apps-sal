def calc_digits(n: int, k: int) -> str:
    if int(n / k):
        return calc_digits(int(n / k), k) + str(n % k)

    return str(n % k)


n, k = list(map(int, input().split()))

print((len(calc_digits(n, k))))
