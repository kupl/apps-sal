from typing import List


class RollingHash:
    __slots__ = ["source", "length", "base", "mod", "hash", "power"]

    def __init__(self, source: str, base: int = 1007, mod: int = 10 ** 9 + 7):
        self.source = source
        self.length = len(source)
        self.base = base
        self.mod = mod
        self.hash = self._get_hash_from_zero()
        self.power = self._get_base_pow()

    def _get_hash_from_zero(self) -> List[int]:
        """Compute hash of interval [0, right)."""
        hash_from_zero = [0] * (self.length + 1)
        cur = 0
        for i, c in enumerate(self.source, 1):
            cur = (cur * self.base + ord(c)) % self.mod
            hash_from_zero[i] = cur
        return hash_from_zero

    def _get_base_pow(self) -> List[int]:
        """Compute mod of power of base."""
        power = [1] * (self.length + 1)
        cur = 1
        for i in range(1, self.length + 1):
            cur *= self.base % self.mod
            power[i] = cur
        return power

    def get_hash(self, left: int, right: int):
        """Compute hash of interval [left, right)."""
        return (
            self.hash[right] - self.hash[left] * self.power[right - left]
        ) % self.mod


def abc141_e():
    # https://atcoder.jp/contests/abc141/tasks/abc141_e
    N = int(input())
    S = input().rstrip()
    rh = RollingHash(S)
    ok, ng = 0, N // 2 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        flg = False
        memo = set()
        for i in range(N - 2 * mid + 1):
            memo.add(rh.get_hash(i, i + mid))
            if rh.get_hash(i + mid, i + 2 * mid) in memo:
                flg = True
                break
        if flg:
            ok = mid  # next mid will be longer
        else:
            ng = mid  # next mid will be shorter
    print(ok)  # max length of substrings appeared twice or more


def __starting_point():
    abc141_e()


__starting_point()
