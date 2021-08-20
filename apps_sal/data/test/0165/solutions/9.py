(b, d, s) = map(int, input().split())


def mins(a, b, c):
    if min([a, b, c]) == a:
        return (a, min(b, c))
    if min([a, b, c]) == b:
        return (b, min(a, c))
    if min([a, b, c]) == c:
        return (c, min(a, b))


ma = max([b, d, s])
(mi1, mi2) = mins(b, d, s)
a1 = max(0, ma - 1 - mi1)
a2 = max(0, ma - 1 - mi2)
print(a1 + a2)
