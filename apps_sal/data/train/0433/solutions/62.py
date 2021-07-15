class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res, curr = 0, 0
        for i, v in enumerate(arr):
            curr += v
            if i >= k:
                curr -= arr[i-k]
            if i >= k-1 and curr / k >= threshold:
                res += 1
        return res
