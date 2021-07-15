R = lambda: map(int, input().split())

def is_vaid(ps, ss, t):
    l, r = 0, max(ps)
    for p, s in zip(ps, ss):
        l, r = max(l, p - s * t), min(r, p + s * t)
    return l < r

n = int(input())
ps, ss = list(R()), list(R())
l, r = 0, max(ps)
while r - l > 10**-6:
    m = (l + r) / 2
    if is_vaid(ps, ss, m):
        r = m
    else:
        l = m
print(r)
