def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
