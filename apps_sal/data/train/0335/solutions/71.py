class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def find(i, diff):
            if i < 0:
                return 0 if diff == 0 else -float('inf')
            return max(
                find(i - 1, diff - rods[i]) + rods[i],
                find(i - 1, diff + rods[i]),
                find(i - 1, diff)
            )
        return find(len(rods) - 1, 0)
