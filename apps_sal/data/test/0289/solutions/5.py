import re


def solve():
    s = input()
    m = 0
    for i in range(len(s)):
        m = max(m, len(re.findall("VK", s[:i] + "V" + s[i + 1:])))
        m = max(m, len(re.findall("VK", s[:i] + "K" + s[i + 1:])))
    print(m)


def __starting_point():
    solve()


__starting_point()
