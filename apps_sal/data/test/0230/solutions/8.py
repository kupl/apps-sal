from collections import defaultdict


class RollingHash(object):

    def __init__(self, S: str, MOD: int = 10 ** 9 + 7, BASE: int = 10 ** 5 + 7):
        self.S = S
        self.N = N = len(S)
        self.MOD = MOD
        self.BASE = BASE
        self.S_arr = [ord(x) for x in S]
        self.POWER = [1] * (N + 1)
        self.HASH = [0] * (N + 1)
        (p, h) = (1, 0)
        for i in range(N):
            self.POWER[i + 1] = p = p * BASE % MOD
            self.HASH[i + 1] = h = (h * BASE + self.S_arr[i]) % MOD

    def hash(self, l: int, r: int):
        _hash = (self.HASH[r] - self.HASH[l] * self.POWER[r - l]) % self.MOD
        return _hash


def main():
    N = int(input())
    S = input()
    MOD = 998244353
    rs = RollingHash(S, MOD=MOD, BASE=37)
    (h, p) = (rs.HASH, rs.POWER)
    (left, right) = (0, N // 2 + 1)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        ok = False
        hash_to_left = defaultdict(list)
        L = mid
        for i in range(N - L + 1):
            _hash = (h[i + L] - h[i] * p[L]) % MOD
            for j in hash_to_left[_hash]:
                if j + L <= i and S[i:i + L] == S[j:j + L]:
                    ok = True
                    break
            if ok:
                break
            hash_to_left[_hash].append(i)
        if ok:
            left = mid
        else:
            right = mid
    print(left)


def __starting_point():
    main()


__starting_point()
