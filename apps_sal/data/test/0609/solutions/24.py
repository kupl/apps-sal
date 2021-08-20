def f():
    n = int(input())
    (k, m) = (n // 2, n - 2)
    t = input()
    (a, b) = (t[0], t[1])
    if a == b:
        return 'NO'
    if t != a + b * m + a:
        return 'NO'
    for i in range(1, k):
        if input() != b * i + a + b * (m - 2 * i) + a + b * i:
            return 'NO'
    if input() != b * k + a + b * k:
        return 'NO'
    for i in range(k - 1, -1, -1):
        if input() != b * i + a + b * (m - 2 * i) + a + b * i:
            return 'NO'
    return 'YES'


print(f())
