class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        w = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])

        x = set()
        for a in fronts:
            if a not in w:
                x.add(a)
        for a in backs:
            if a not in w:
                x.add(a)

        if not x:
            return 0
        return min(x)
