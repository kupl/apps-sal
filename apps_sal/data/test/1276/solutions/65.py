def main():
    n = int(input())
    s = input()
    ans = s.count('R') * s.count('G') * s.count('B')
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if j - i > n - j - 1:
                break
            if s[i] != s[j] and s[j] != s[2 * j - i] and (s[2 * j - i] != s[i]):
                ans -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
