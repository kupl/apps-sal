class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # r need be max(arr) + 1, not target
        l, r, minDiff, res = 0, max(arr) + 1, float('inf'), float('inf')
        while l < r:
            m = l + (r - l) // 2
            # m is too big, since few num are reduced to m.
            currSum = 0
            for n in arr:
                currSum += min(m, n)
            if currSum == target:
                return m
            currDiff = abs(target - currSum)
            if currDiff < minDiff:
                minDiff = currDiff
                res = m
            elif currDiff == minDiff:
                res = min(res, m)
            if currSum > target:
                r = m
            else:
                l = m + 1
        return res
            
    # https://www.youtube.com/watch?v=j0KejYpI_Mc
    def findBestValue1(self, arr: List[int], target: int) -> int:
        arr.sort()
        length = len(arr)
        for n in arr:
            # round is different to //. round(1.2) = 1, round(1.6) = 2
            res = round(target / length)
            if n >= res:
                return res
            target -= n
            length -= 1
        # return biggest num
        return arr[-1]
