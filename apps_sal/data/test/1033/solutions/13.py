def S(l):
    return l * (l + 1) // 2


def f(l, h):
    if l <= h:
        return S(l)
    s = S(h)
    l -= h
    s += l * h
    s += S(l // 2) + S(l // 2 - (1 - l % 2))
    return s


n, H = list(map(int, input().split()))

l = 0
r = n + 1

while r - l > 1:
    md = (l + r) // 2
    if f(md, H) >= n:
        r = md
    else:
        l = md

print(r)
