def main():
    n = int(input())

    def get_divisors(num):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.extend([i, num // i])
        return set(divisors)
    ans = len(get_divisors(n - 1)) - 1
    for k in get_divisors(n):
        if k == 1:
            continue
        num = n
        while num % k == 0:
            num = num // k
        if num % k == 1:
            ans += 1
    print(ans)


main()
