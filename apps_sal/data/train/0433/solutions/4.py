class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        cur = 0
        res = 0
        for i in range(k):
            cur += arr[i]
        if cur / k >= threshold:
            res += 1
        for i in range(k, len(arr)):
            cur = cur + arr[i] - arr[i - k]
            if cur / k >= threshold:
                res += 1
        return res
