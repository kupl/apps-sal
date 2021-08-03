class Solution:
    def totalFruit(self, trees: List[int]) -> int:

        if len(trees) <= 2:
            return len(trees)

        lp = 0
        rp = 1
        maxSize = 0
        hash = collections.defaultdict(int)
        lpInc = False
        rpInc = False
        curSet = set()

        # Start the left and right pointer values at 1 frequency. Use += 1 in case trees[lp] and trees[rp] point to the same value.
        hash[trees[lp]] += 1
        curSet.add(trees[lp])
        hash[trees[rp]] += 1
        curSet.add(trees[rp])

        while rp < len(trees):
            if lpInc:
                hash[trees[lp - 1]] = max(hash[trees[lp - 1]] - 1, 0)
                if hash[trees[lp - 1]] > 0:
                    curSet.add(trees[lp - 1])
                else:
                    curSet.remove(trees[lp - 1])
            if rpInc:
                hash[trees[rp]] += 1
                curSet.add(trees[rp])

            lpInc = False
            rpInc = False

            if len(curSet) <= 2:
                if (rp - lp) + 1 > maxSize:
                    maxSize = (rp - lp) + 1

            if len(curSet) > 2:
                lp += 1
                lpInc = True
            else:
                rp += 1
                rpInc = True

        return maxSize
