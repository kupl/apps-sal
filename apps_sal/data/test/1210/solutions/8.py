(n, p) = [int(x) for x in input().split()]
segments = []
for i in range(n):
    segments.append(tuple((int(x) for x in input().split())))


def divam(p, s):
    return (s[1] - s[0]) // p + (s[1] % p < s[0] % p or s[0] % p == 0)


def expectation(s1, s2):
    (k1, k2) = (divam(p, s1), divam(p, s2))
    (n1, n2) = (s1[1] - s1[0] + 1, s2[1] - s2[0] + 1)
    return 2000 * (k1 * n2 + k2 * n1 - k1 * k2) / (n1 * n2)


print(sum((expectation(segments[i], segments[(i + 1) % n]) for i in range(n))))
