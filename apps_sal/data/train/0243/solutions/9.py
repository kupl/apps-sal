class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        not_allowed = set()
        for f, b in zip(fronts, backs):
            if f == b:
                not_allowed.add(f)
        res = math.inf
        for f, b in zip(fronts, backs):
            if f not in not_allowed:
                res = min(res, f)
            if b not in not_allowed:
                res = min(res, b)
        if math.isfinite(res):
            return res
        else:
            return 0
