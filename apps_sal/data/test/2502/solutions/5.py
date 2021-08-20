import sys
sys.setrecursionlimit(10 ** 6)


def rolling_hash(s, w, MOD):
    ret = []
    tmp = 0
    p = pow(26, w, MOD)
    ords = [ord(c) - 97 for c in s]
    for (i, o) in enumerate(ords):
        tmp = tmp * 26 + o
        if i >= w:
            tmp = tmp - ords[i - w] * p
        tmp %= MOD
        ret.append(tmp)
    return ret


def solve(s, t):
    MOD = 10 ** 9 + 7
    (ls, lt) = (len(s), len(t))
    k = (lt - 1) // ls + 1
    s *= k * 2
    ls *= k
    (rs, rt) = (rolling_hash(s, lt, MOD), rolling_hash(t, lt, MOD))
    rs = rs[ls:]
    ht = rt[-1]
    checked = [-1] * ls

    def series(i, st):
        if st <= i < st + lt:
            return float('-inf')
        if checked[i] == -1:
            checked[i] = series((i + lt) % ls, st) + 1 if rs[i] == ht else 0
        return checked[i]
    for (i, hs) in enumerate(rs):
        if hs != ht:
            continue
        ret = series((i + lt) % ls, i)
        if ret == float('-inf'):
            return -1
        checked[i] = ret + 1
    return max(0, max(checked))


s = input()
t = input()
print(solve(s, t))
