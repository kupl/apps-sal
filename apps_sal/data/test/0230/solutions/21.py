from typing import List, Tuple


class RollingHash:
    """Rolling Hash"""
    __slots__ = ['_base', '_mod', '_hash', '_power']

    def __init__(self, source: str, base: int = 1007, mod: int = 10 ** 9 + 7):
        self._base = base
        self._mod = mod
        (self._hash, self._power) = self._build(source)

    def _build(self, source: str) -> Tuple[List[int], List[int]]:
        """Compute "hash" and "mod of power of base" of interval [0, right)."""
        (hash_, power) = ([0] * (len(source) + 1), [0] * (len(source) + 1))
        power[0] = 1
        for (i, c) in enumerate(source, 1):
            hash_[i] = (hash_[i - 1] * self._base + ord(c)) % self._mod
            power[i] = power[i - 1] * self._base % self._mod
        return (hash_, power)

    def get_hash(self, left: int, right: int):
        """Return hash of interval [left, right)."""
        return (self._hash[right] - self._hash[left] * self._power[right - left]) % self._mod


def abc141_e():
    N = int(input())
    S = input().rstrip()
    rh = RollingHash(S)
    (ok, ng) = (0, N // 2 + 1)
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
