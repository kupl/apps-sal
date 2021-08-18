from typing import List


class RollingHash:
    __slots__ = ["_source", "_length", "_base", "_mod", "_hash", "_power"]

    def __init__(self, source: str, base: int = 1007, mod: int = 10 ** 9 + 7):
        self._source = source
        self._length = len(source)
        self._base = base
        self._mod = mod
        self._hash = self._get_hash_from_zero()
        self._power = self._get_base_pow()

    def _get_hash_from_zero(self) -> List[int]:
        """Compute hash of interval [0, right)."""
        hash_from_zero = [0] * (self._length + 1)
        cur = 0
        for i, c in enumerate(self._source, 1):
            cur = (cur * self._base + ord(c)) % self._mod
            hash_from_zero[i] = cur
        return hash_from_zero

    def _get_base_pow(self) -> List[int]:
        """Compute mod of power of base."""
        power = [0] * (self._length + 1)
        power[0] = 1
        cur = 1
        for i in range(1, self._length + 1):
            cur *= self._base % self._mod
            power[i] = cur
        return power

    def get_hash(self, left: int, right: int):
        """Compute hash of interval [left, right)."""
        return (
            self._hash[right] - self._hash[left] * self._power[right - left]
        ) % self._mod


def abc141_e():
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
            ok = mid
        else:
            ng = mid
    print(ok)


def __starting_point():
    abc141_e()


__starting_point()
