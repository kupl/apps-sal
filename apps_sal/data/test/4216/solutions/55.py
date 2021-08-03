
url = "https://atcoder.jp//contests/abc057/tasks/abc057_c"


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    n = int(input())
    ans = 10000000000000000
    ns = make_divisors(n)
    for i in range(0, (len(ns) // 2) + 1):
        tmp = max(len(str(ns[i])), len(str(ns[len(ns) - i - 1])))
        ans = tmp if tmp < ans else ans
    if len(ns) % 2 != 0:
        tmp = len(str(ns[len(ns) // 2]))
        ans = tmp if tmp < ans else ans
    print(ans)


def __starting_point():
    main()


__starting_point()
