class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cands = [0] * 2001
        blacklist = [0] * 2001
        for (f, b) in zip(fronts, backs):
            if f == b:
                blacklist[f] = 1
                cands[b] = 0
            else:
                if not blacklist[f]:
                    cands[f] = 1
                if not blacklist[b]:
                    cands[b] = 1
        for idx in range(1, 2001):
            if cands[idx]:
                return idx
        return 0
