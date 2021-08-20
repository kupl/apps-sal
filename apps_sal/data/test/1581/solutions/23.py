from itertools import accumulate


def f(n, k):
    lim = int((n + 0.1) ** 0.5) + 1
    ws = []
    s = 0
    for i in range(1, lim):
        w = n // i - n // (i + 1)
        ws.append(w)
        s += w
    ws += [1] * (n - s)
    dp = ws
    m = len(ws)
    for _ in range(k - 1):
        dp = [s * w % md for (s, w) in zip(accumulate(dp[::-1]), ws)]
    print(sum(dp) % md)


md = 10 ** 9 + 7
(n, k) = list(map(int, input().split()))
f(n, k)
