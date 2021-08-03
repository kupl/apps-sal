s = input()
n = len(s)


def f(s):
    return s == s[::-1]


if f(s) and f(s[:(n - 1) // 2]) and f(s[(n + 3) // 2 - 1:]):
    print("Yes")
else:
    print("No")
