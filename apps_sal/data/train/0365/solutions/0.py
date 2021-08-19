class Solution:
    def uniqueLetterString(self, s: str) -> int:
        chrLoc = defaultdict(list)
        ct = 0
        md = 1000000007
        l = len(s)
        for i, c in enumerate(s):
            chrLoc[c].append(i)

        for c in chrLoc:
            locs = [-1] + chrLoc[c] + [l]
            loc_ct = len(locs)
            #print(c, locs)
            for i in range(1, loc_ct - 1):
                leftWingSpan = locs[i] - locs[i - 1]  # i-mostRecently + 1
                rightWingSpan = locs[i + 1] - locs[i]  # l-i
                ct += ((leftWingSpan % md) * (rightWingSpan % md)) % md
                #print(leftWingSpan,rightWingSpan, c, i)
                ct %= md

        return ct
