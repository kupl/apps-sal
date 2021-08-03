class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        N = len(fronts)
        impossible = set([fronts[i] for i in range(N) if fronts[i] == backs[i]])
        res = float('inf')
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                for num in [fronts[i], backs[i]]:
                    if num not in impossible:
                        res = min(res, num)
        return res if res != float('inf') else 0
