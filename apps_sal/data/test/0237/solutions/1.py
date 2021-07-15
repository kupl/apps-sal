def v(ln, mx):
    return mx * (mx + 1) // 2 - (0 if ln > mx else (mx - ln) * (mx - ln + 1) // 2) + max(0, ln - mx)

def ok(n, m, k, val):
    return val + v(k - 1, val - 1) + v(n - k, val - 1) <= m


n, m, k = map(int, input().split())
l = -1
r = 10 ** 10
while l + 1 != r:
    md = (l + r) // 2
    if ok(n, m, k, md):
        l = md
    else:
        r = md
print(l)
