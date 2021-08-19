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
        _hash = self.HASH[r] - self.HASH[l] * self.POWER[r - l] % self.MOD
        if _hash < 0:
            _hash += self.MOD
        return _hash


def binary_search(left: int, right: int, check_func, search_max: bool = False):
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if check_func(mid) ^ search_max:
            right = mid
        else:
            left = mid
    return left if search_max else right


def main():
    N = int(input())
    S = input()
    rs = RollingHash(S, MOD=998244353, BASE=37)

    def isOK(L):
        if L == 0:
            return True
        hash_to_left = defaultdict(list)
        for i in range(N - L + 1):
            _hash = rs.hash(i, i + L)
            for j in hash_to_left[_hash]:
                if j + L <= i and S[i:i + L] == S[j:j + L]:
                    return True
            hash_to_left[_hash].append(i)
        return False
    ans = binary_search(0, N // 2 + 1, isOK, search_max=True)
    print(ans)


def __starting_point():
    main()


__starting_point()
