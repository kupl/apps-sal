mod = 10 ** 9 + 7


def solve(n: str, k: int):
    out = 0
    if k == 0:
        out = 1
    elif k == 1:
        out = len(n) - 1
    elif k == 2:
        for i in range(1, min(len(n), 10)):
            x = 2 ** i
            cnt = 0
            for j in range(len(n)):
                if n[j] == '1':
                    out += C(len(n) - j - 1, x - cnt)
                    out %= mod
                    cnt += 1
            if n.count('1') == x:
                out += 1
    elif 3 <= k <= 5:
        d = dict()
        cnt = 0
        for i in range(len(n)):
            if n[i] == '1':
                m = 1
                for j in range(len(n) - i):
                    assertadd(d, j + cnt, m)
                    m *= len(n) - i - j - 1
                    m //= j + 1
                cnt += 1
        assertadd(d, n.count('1'), 1)
        for key in d:
            out += d[key] * recur(key, k - 1)
        out %= mod
    elif k >= 6:
        out = 0
    return out


def assertadd(d: dict, k, v):
    try:
        d[k] += v
    except:
        d[k] = v


def recur(k, level):
    for i in range(level):
        k = bin(k)[2:].count('1')
        if k == 1 and i != level - 1:
            return 0
    return 1 if k == 1 else 0


def C(n, k):
    if k < 0 or k > n:
        return 0
    out = 1
    for i in range(k):
        out *= n - i
        out //= i + 1
    return out % mod


def __starting_point():
    n = input()
    k = int(input())
    print(solve(n, k))


__starting_point()
