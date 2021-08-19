(n, k) = map(int, input().split())
a = list(map(int, input().split()))


def ok(d):
    m = sorted((a % d for a in a))
    (s, e, plus, minus) = (0, len(m) - 1, 0, 0)
    while True:
        if s > e:
            return plus == minus
        if plus <= minus:
            plus += m[s]
            if plus > k:
                return False
            s += 1
        else:
            minus += d - m[e]
            if minus > k:
                return False
            e -= 1
    return False


b = sum(a)
ret = 1
d = 1
while d * d <= b:
    if b % d == 0:
        if ok(d):
            ret = max(ret, d)
        if ok(b // d):
            ret = max(ret, b // d)
    d += 1
print(ret)
