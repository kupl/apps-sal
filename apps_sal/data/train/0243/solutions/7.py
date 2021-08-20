class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        dupes = {fronts[i] for i in range(n) if fronts[i] == backs[i]}
        res = float('inf')
        for num in itertools.chain(fronts, backs):
            if num not in dupes:
                res = min(res, num)
        return res if res < float('inf') else 0
