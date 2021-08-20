class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        (l, r) = (0, k - 1)
        res = 0
        s = sum(arr[:k])
        t = threshold * k
        while r < len(arr):
            if s >= t:
                res += 1
            if r + 1 < len(arr):
                s = s - arr[l] + arr[r + 1]
            l += 1
            r += 1
        return res
