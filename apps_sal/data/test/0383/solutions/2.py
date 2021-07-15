import collections


def count(n, k):

    m = collections.defaultdict(lambda: 0)
    m[0] = 1
    for i in range(1, n + 1):

        for j in range(1, k + 1):

            if i - j in m:

                m[i] += m[i - j]

    return m[n]

n, k, d = tuple(map(int, str.split(input())))
print((count(n, k) - count(n, d - 1)) % (10 ** 9 + 7))

