class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        ans = len(c)
        for v in sorted(c.values()):
            if v <= k:
                ans -= 1
                k -= v
        return ans
