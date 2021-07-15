class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounts = collections.defaultdict(int)
        tCounts = collections.defaultdict(int)
        for c in s:
            sCounts[c] += 1
        for c in t:
            tCounts[c] += 1
        change = 0
        for k in tCounts:
            if k not in sCounts:
                change += tCounts[k]
            elif k in sCounts and sCounts[k] < tCounts[k]:
                change += tCounts[k] - sCounts[k]

        return change
