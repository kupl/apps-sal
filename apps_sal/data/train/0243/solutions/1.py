class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for (x, y) in zip(fronts, backs) if x == y}
        return min([i for i in fronts + backs if i not in same] or [0])
