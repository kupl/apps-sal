class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen=set()
        double=set()
        for i in range(len(fronts)):
            seen.add(fronts[i])
            seen.add(backs[i])
            if fronts[i]==backs[i]:
                double.add(fronts[i])
        for k in sorted(list(seen)):
            if not k in double:
                return k
        return 0

