n = int(input())
aa = ord(input()) - 65
ab = ord(input()) - 65
ba = ord(input()) - 65
bb = ord(input()) - 65
mo = 10**9 + 7


def f(a):
    r = 1
    for i in range(1, a + 1):
        r *= i
    return r


def c(a, b):
    return f(a) // f(b) // f(a - b)


if ab == 0:
    ab = 1
    ba = 1 - ba
    bb = 1 - aa
if n == 2:
    print((1))
elif bb == 1:
    print((1))
elif ba == 0:
    print((2 ** (n - 3) % mo))
else:
    m = n - 3
    s = 0
    for i in range(0, m + 1):
        if i > m + 1 - i:
            break
        s += c(m + 1 - i, i)
    print((s % mo))
