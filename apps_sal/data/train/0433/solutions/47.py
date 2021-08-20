class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        (s, ans) = (0, 0)
        for (i, num) in enumerate(arr):
            if i < k:
                s += num
                continue
            if s >= target:
                ans += 1
            s = s - arr[i - k] + arr[i]
        if s >= target:
            ans += 1
        return ans
