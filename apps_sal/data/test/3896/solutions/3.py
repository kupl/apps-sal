t = input()
(n, d) = (len(t), 1000000007)


def f(k):
    return 0 if k == n else 2 * f(k + 1) + (pow(2, 2 * (n - k - 1), d) if t[k] == '1' else 0)


print(f(0) % d)
