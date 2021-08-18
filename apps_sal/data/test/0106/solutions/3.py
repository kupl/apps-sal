n, m, k = map(int, input().split())
kv1, kv2 = map(int, input().split())
kv1 -= 1
kv2 -= 1
p1 = (kv1) // (m * k)
p2 = (kv2) // (m * k)
kv1 %= k * m
kv2 %= k * m
at1 = kv1 // k
at2 = kv2 // k
if (p1 == p2):
    print(min(10 + abs(at1 - at2), 5 * abs(at1 - at2)))
else:
    res = 15 * min(abs(p1 - p2), min(p1, p2) + n - max(p1, p2))
    res += min(10 + at1, at1 * 5)
    res += min(10 + at2, at2 * 5)
    print(res)
