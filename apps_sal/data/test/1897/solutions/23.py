def sum_vowels(s, i, j):
    ans = 0

    for index in range(i, j + 1):
        if s[index] in "AEIOUY":
            ans += 1

    return ans


def __starting_point():
    s = input()
    n = len(s)

    ans = 0

    num = 0
    den_inv = 0
    prev_sum = sum_vowels(s, 0, n - 1)
    for i in range(int(n / 2)):
        num += prev_sum
        den_inv = 1 / (i + 1) + 1 / (n - i)

        ans += num * den_inv

        if s[i] in "AEIOUY":
            prev_sum -= 1
        if s[n - 1 - i] in "AEIOUY":
            prev_sum -= 1

    if (n % 2 == 1):
        i = int(n / 2)
        num += sum_vowels(s, i, i)
        den_inv = 1 / (i + 1)

        ans += num * den_inv

    print("{:.6f}".format(ans))


__starting_point()
