class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        window = 0
        ans = 0
        for r, num in enumerate(arr):
            window += num
            if r >= k:
                window -= arr[r - k]
            if r >= k - 1 and window >= threshold:
                ans += 1
        return ans
