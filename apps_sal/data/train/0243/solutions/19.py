from collections import defaultdict


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        if len(fronts) == 1:
            if fronts[0] == backs[0]:
                return 0
            else:
                return fronts[0]
        f, b = defaultdict(set), defaultdict(set)
        for i in range(len(fronts)):
            f[fronts[i]].add(backs[i])
            b[backs[i]].add(fronts[i])

        ans = float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in f[fronts[i]]:
                ans = min(ans, fronts[i])
            if backs[i] not in b[backs[i]]:
                ans = min(ans, backs[i])

        if ans == float('inf'):
            return 0
        return ans
