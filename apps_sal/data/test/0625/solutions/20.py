__author__ = 'Rakshak.R.Hegde'


def AP(a, n, d):
    return n * (2 * a + (n - 1) * d) >> 1


n = int(input())
ans = AP(2, n >> 1, 2) - AP(1, n + 1 >> 1, 2)
print(ans)
