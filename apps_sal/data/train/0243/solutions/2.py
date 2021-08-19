class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cands = set()
        blacklist = set()
        for (f, b) in zip(fronts, backs):
            if f == b:
                blacklist.add(f)
                cands.discard(f)
            else:
                if f not in blacklist:
                    cands.add(f)
                if b not in blacklist:
                    cands.add(b)
        return 0 if not cands else min(cands)
