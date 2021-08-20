class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        m = sorted(d.values())
        ans = len(m)
        for c in m:
            if k >= c:
                k -= c
                ans -= 1
        return ans
