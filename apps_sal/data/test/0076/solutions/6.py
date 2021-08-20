def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, m, a, b) = mi()
d = n % m
c1 = d * b
c2 = (m - d) * a
print(min(c1, c2))
