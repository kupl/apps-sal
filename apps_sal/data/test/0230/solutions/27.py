class RollingHash:
    """Rolling Hash"""

    __slots__ = ["_base", "_mod", "_hash", "_power"]

    def __init__(self, source: str, base: int = 1007, mod: int = 10 ** 9 + 7) -> None:
        self._base = base
        self._mod = mod
        self._hash = [0] * (len(source) + 1)
        self._power = [0] * (len(source) + 1)

        self._power[0] = 1
        for i, c in enumerate(source, 1):
            self._hash[i] = (self._hash[i - 1] * self._base + ord(c)) % self._mod
            self._power[i] = self._power[i - 1] * self._base % self._mod

    def get_hash(self, left: int, right: int) -> int:
        """Return hash of interval [left, right)."""
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
