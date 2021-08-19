from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def __starting_point():
    (t, w, b) = list(map(int, input().split()))
    l = lcm(w, b)
    m = min(w, b)
    count = t // l
    result = count * m
    result += m - 1
    diff = max(count * l + m - t - 1, 0)
    result -= diff
    g = gcd(result, t)
    print('{}/{}'.format(result // g, t // g))


__starting_point()
