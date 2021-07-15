class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        dupes = set(fronts[i] for i in range(n) if fronts[i] == backs[i])
        res = float('inf')
        for i in range(n):
            if fronts[i] not in dupes:
                res = min(res, fronts[i])
            if backs[i] not in dupes:
                res = min(res, backs[i])
        return res if res < float('inf') else 0
