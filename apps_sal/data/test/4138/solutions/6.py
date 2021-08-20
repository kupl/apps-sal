def l(n):
    s = 0
    for i in range(20):
        o = 10 ** i - 1
        if o > n:
            break
        s += (n - o) * (n - o + 1) // 2
    return s


def bs(k):
    n = 0
    for p in range(63, -1, -1):
        if l(n + 2 ** p) < k:
            n += 2 ** p
    return n


def num(n):
    if n < 10:
        return n
    for i in range(1, 19):
        seglen = i * 9 * 10 ** (i - 1)
        if n <= seglen:
            return str(10 ** (i - 1) + (n - 1) // i)[(n - 1) % i]
        else:
            n -= seglen


q = int(input())
for _ in range(q):
    k = int(input())
    print(num(k - l(bs(k))))
