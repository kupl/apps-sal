def prime_decomposition(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append((i, n / i))
        i += 1
    return ans


def main():
    S, P = map(int, input().split())
    kouho = prime_decomposition(P)
    a = "No"
    for i in kouho:
        if sum(i) == S:
            a = "Yes"
    print(a)


def __starting_point():
    main()


__starting_point()
