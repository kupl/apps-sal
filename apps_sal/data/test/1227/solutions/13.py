def nCkpow(n, k):
    if n < k:
        return 0
    y = 1
    for i in range(k):
        y *= n - i
        y //= i + 1
        y *= 9
    return y


def f(s, m, k):
    # print(m,k)
    if len(s) - m < k:
        return 0
    if k == 0:
        return 1
    if s[m] == '0':
        return f(s, m + 1, k)
    l = len(s) - m
    y = nCkpow(l - 1, k)
    y += (int(s[m]) - 1) * nCkpow(l - 1, k - 1)
    return y + f(s, m + 1, k - 1)


N = input()
K = int(input())
print(f(N, 0, K))
