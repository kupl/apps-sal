class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        if not rods:
            return 0

        rods.sort()
        l = len(rods)

        @lru_cache(maxsize=None)
        def search(idx, diff):
            if idx < 0:
                if diff == 0:
                    return True, 0
                else:
                    return False, 0

            f1, v1 = search(idx - 1, diff - rods[idx])
            f2, v2 = search(idx - 1, diff + rods[idx])

            if f1 and f2:
                return True, max(v1, v2) + rods[idx]
            elif f1:
                return True, v1 + rods[idx]
            elif f2:
                return True, v2 + rods[idx]
            return search(idx - 1, diff)

        return search(l - 1, 0)[1] // 2
