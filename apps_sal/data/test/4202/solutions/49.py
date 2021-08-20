def main():
    (l, r) = map(int, input().split())
    (q, ll) = (l // 2019, l % 2019)
    rr = r % 2019
    rng = [*range(ll, rr + 1)] if r - l < (2019 * q - ll) % 2019 else [*range(ll, 2019)] + [*range(rr + 1)]
    lenrng = len(rng)
    ans = 2020
    for i in range(lenrng - 1):
        for j in range(i + 1, lenrng):
            tmp = rng[i] * rng[j] % 2019
            if tmp < ans:
                ans = tmp
    print(ans)


def __starting_point():
    main()


__starting_point()
