class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s = set(fronts).union(set(backs))
        
        for c in sorted(s):
            for i in range(len(fronts)):
                if fronts[i] == c and backs[i] == c:
                    break
            else:
                return c
        return 0
