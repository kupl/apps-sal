class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        exclusions = {x for (x, y) in zip(fronts, backs) if x == y}
        ans = float('inf')
        for (x, y) in zip(fronts, backs):
            if not (x in exclusions and y in exclusions):
                if x not in exclusions:
                    ans = min(ans, x)
                if y not in exclusions:
                    ans = min(ans, y)
        return ans if ans != float('inf') else 0
