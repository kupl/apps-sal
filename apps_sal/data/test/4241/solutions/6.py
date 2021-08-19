def b177(s, t):
    ans = 10 ** 8
    for i in range(len(s) - len(t) + 1):
        count = 0
        for w in range(len(t)):
            if s[i + w] == t[w]:
                count += 1
        ans = min(ans, len(t) - count)
    return ans


def main():
    s = list(str(input()))
    t = list(str(input()))
    print(b177(s, t))


def __starting_point():
    main()


__starting_point()
