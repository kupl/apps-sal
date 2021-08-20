(q, w) = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0 for i in range(0, q + 1)]


def f(q, w, pos):
    d = 1
    if w >= pos:
        d += pos - 1
    else:
        d += w
    if pos >= q - w:
        d += q - pos
    else:
        d += w
    return d


def g(q, w, i, j):
    ans = w * 2 - j + i + 1
    if j - w <= 0:
        ans -= w - j + 1
    if i + w > q:
        ans -= i + w - q
    return ans


for i in range(1, q + 1):
    if a[i] == 0:
        s[i] = f(q, w, i)
    else:
        t = i - a[i]
        if t > 2 * w:
            s[i] = f(q, w, i) + s[a[i]]
        else:
            s[i] = s[a[i]] + f(q, w, i) - g(q, w, a[i], i)
print(*s[1:])
