import random


def alg(n, k):
    best = None
    last_digit = 9 - k
    ks = (k * (k + 1)) // 2
    if ks <= n:
        ts = n - ks
        if ts % (k + 1) == 0:
            s = ts // (k + 1)
            if last_digit >= s:
                best = min(s, last_digit)
            else:
                num = str(last_digit)
                s -= last_digit
                while s > 0:
                    r = min(s, 9)
                    s -= r
                    num = str(r) + num
                best = int(num)
    for d in range(1, 100):
        for j in range(1, k + 1):
            tn = n + 9 * d * (k - j + 1)
            ts = tn - ks
            s = ts // (k + 1)
            req = 9 * (d - 1) + 10 - j
            if s < req:
                continue
            if ts % (k + 1) == 0:
                num = "9" * (d - 1) + str(10 - j)
                rem = s - req
                if rem > 8:
                    num = "8" + num
                    rem -= 8
                while rem > 0:
                    r = min(rem, 9)
                    rem -= r
                    num = str(r) + num
                if best is None:
                    best = int(num)
                else:
                    best = min(best, int(num))
    if best is None:
        return -1
    return best


t = int(input())

tc = []
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    tc.append((n, k))


for n, k in tc:
    print(alg(n, k))
