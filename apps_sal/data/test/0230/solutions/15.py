from collections import defaultdict


class RollingHash(object):
    def __init__(self, S: str, MOD: int = 10 ** 9 + 7, BASE: int = 10 ** 5 + 7):
        self.S = S
        self.N = N = len(S)
        self.MOD = MOD
        self.BASE = BASE

        S_arr = [ord(x) for x in S]
        POWER = [1] * (N + 1)
        HASH = [0] * (N + 1)
        p, h = 1, 0
        for i in range(N):
            POWER[i + 1] = p = (p * BASE) % MOD
            HASH[i + 1] = h = (h * BASE + S_arr[i]) % MOD
        self.S_arr = S_arr
        self.POWER = POWER
        self.HASH = HASH

    def hash(self, l: int, r: int):
        # get hash for S[l:r]
        _hash = (self.HASH[r] - self.HASH[l] * self.POWER[r - l]) % self.MOD
        return _hash


def main():
    N = int(input())
    S = input()
    MOD = 998244353
    rs = RollingHash(S, MOD=MOD, BASE=37)
    h, p = rs.HASH, rs.POWER

    left, right = 0, N // 2 + 1
    D = [0] * N
    while abs(right - left) > 1:
        mid = (left + right) // 2
        # hash_to_left = defaultdict(list)
        hashes = set()
        L = mid
        P = p[L]
        for i in range(min(L, N - 2 * L + 1)):
            D[i] = (h[L + i] - h[i] * P) % MOD
        hashes = set()
        ok = False
        for i in range(L, N - L + 1):
            hashes.add(D[i - L])
            D[i] = v = (h[L + i] - h[i] * P) % MOD
            if v in hashes:
                ok = True
                break
        if ok:
            left = mid
        else:
            right = mid

    print(left)


def __starting_point():
    main()


__starting_point()
