n, m, k = map(int, input().split())


def z():
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                yield i + 1, j + 1
            else:
                yield i + 1, m - j


def p(a):
    print(len(a), ' '.join("{} {}".format(x, y) for x, y in a))


a = list(z())
l = n * m // k
for i in range(k - 1):
    p(a[i * l: (i + 1) * l])
p(a[l * (k - 1):])
