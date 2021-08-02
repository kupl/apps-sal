n = input()
a, b, c, d, e, f = list(map(int, n))


def g(a, b, c, s):
    m1, m2, m3 = sorted([a, b, c])
    if s == a + b + c:
        return 0
    elif s > a + b + c:
        s1 = a + b + c
        if m2 + m3 + 9 >= s:
            return 1
        if m3 + 18 >= s:
            return 2
        else:
            return 3
    else:
        if m1 + m2 <= s:
            return 1
        if m1 <= s:
            return 2
        return 3


ll = []
for s in range(28):
    ll.append(g(a, b, c, s) + g(d, e, f, s))

print(min(ll))
