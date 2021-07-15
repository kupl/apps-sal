class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(maxsize=None)
        def solve(i: int, s: int) -> int:            
            if i >= len(rods):
                return 0 if s == 0 else -math.inf
            
            return max(solve(i + 1, s), solve(i + 1, s - rods[i]), rods[i] + solve(i + 1, s + rods[i]))
        
        return 0 if math.isinf(res := solve(0, 0)) else res
