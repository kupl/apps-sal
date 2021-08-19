def main():
    S = input()[::-1]
    counts = [0] * 2019
    counts[0] = 1
    (res, digit) = (0, 1)
    for i in S:
        res += int(i) * digit
        res %= 2019
        digit *= 10
        digit %= 2019
        counts[res] += 1
    ans = 0
    for i in counts:
        ans += i * (i - 1) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
