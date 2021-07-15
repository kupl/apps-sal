from math import ceil

n, a, b = list(map(int, input().split()))
hs = [int(input()) for _ in range(n)]


def defeatable(k):
    hb = [max([h - k * b, 0]) for h in hs]
    n_attack = sum([ceil(h / (a - b)) for h in hb])
    return n_attack <= k


l, r = 0, ceil(max(hs) / b)

while r - l > 1:
    m = (l + r) // 2

    if defeatable(m):
        r = m
    else:
        l = m

print(r)


