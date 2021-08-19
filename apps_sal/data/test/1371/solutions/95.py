s = int(input())
t = 1 if s >= 3 else 0
M = 10 ** 9 + 7
S = [1] + [0] * 2000


def cmb(n, r):
    (c, m) = (1, 1)
    for i in range(1, r + 1):
        c = c * (n - i + 1) % M
        m = m * i % M
    return c * pow(m, M - 2, M) % M


for i in range(2, s // 3 + 1):
    t = (t + cmb(s - 2 * i - 1, i - 1)) % M
print(t)
