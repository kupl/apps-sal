class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def count(n, idxCnt):
            if not n:
                return 1
            (idx, cnt) = idxCnt
            out = 0
            for i in range(6):
                times = rollMax[i]
                if idx == i:
                    if times > cnt:
                        out += count(n - 1, (i, cnt + 1))
                else:
                    out += count(n - 1, (i, 1))
            return out
        return count(n, (0, 0)) % 1000000007
