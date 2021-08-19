3
# -*- coding: utf8 -*-


def main():
    s = list(map(int, input()))
    ans = []
    while max(s) != 0:
        t = []
        for i in range(len(s)):
            t.append('1' if s[i] else '0')
            s[i] = max(0, s[i] - 1)
        ans.append(t)
    print(len(ans))
    print(' '.join([''.join(_).lstrip('0') for _ in ans]))


def __starting_point():
    main()


__starting_point()
