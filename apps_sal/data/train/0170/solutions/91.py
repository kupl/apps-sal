class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ndpreflen = 1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break
            ndpreflen += 1
        ndsufflen = 1
        for i in range(1, n):
            if arr[n - 1 - i] > arr[n - i]:
                break
            ndsufflen += 1
        if ndpreflen + ndsufflen > n:
            return 0
        sufffirstkeep_idx = n - ndsufflen
        ans = min(n - ndpreflen, n - ndsufflen)
        for preflastkeep_idx in range(ndpreflen):
            while sufffirstkeep_idx < n and arr[sufffirstkeep_idx] < arr[preflastkeep_idx]:
                sufffirstkeep_idx += 1
            if sufffirstkeep_idx == n:
                break
            ans = min(ans, sufffirstkeep_idx - preflastkeep_idx - 1)
        return ans
