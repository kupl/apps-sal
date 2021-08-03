class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        res, occ = 0, collections.defaultdict(int)

        for r in range(len(s) - minSize + 1):

            sub = s[r:r + minSize]

            if len(set(sub)) <= maxLetters:

                occ[sub] += 1
                res = max(res, occ[sub])

        return(res)
