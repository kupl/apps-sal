class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        offlimits = set()
        for f, b in zip(fronts, backs):
            if f == b:
                offlimits.add(f)
        ans = math.inf
        for f, b in zip(fronts, backs):
            if f != b:
                if f not in offlimits:
                    ans = min(ans, f)
                if b not in offlimits:
                    ans = min(ans, b)

        return 0 if ans == math.inf else ans
