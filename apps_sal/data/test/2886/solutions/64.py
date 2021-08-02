s = input()
n = len(s)


def solve():
    for i in range(1, n):
        if s[i - 1] == s[i]:
            print((i, i + 1))
            return
    for i in range(2, n):
        if s[i - 2] == s[i - 1] or s[i - 1] == s[i] or s[i - 2] == s[i]:
            print((i - 1, i + 1))
            return
    print((-1, -1))


if n == 2:
    if s[0] == s[1]:
        print((1, 2))
    else:
        print((-1, -1))
else:
    solve()
