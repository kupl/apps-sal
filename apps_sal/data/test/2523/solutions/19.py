import sys
#input = sys.stdin.buffer.readline


def main():
    s = input()
    l = len(s)
    if "0" not in s or "1" not in s:
        print(l)
    else:
        ans = 10**6
        for i in range(l - 1):
            if s[i] != s[i + 1]:
                ans = min(ans, max(i + 1, l - i - 1))
        print(ans)


def __starting_point():
    main()


__starting_point()
