class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = 0
        threshold = k * threshold
        if len(arr) < k:
            return 0
        else:
            for i in range(k):
                total += arr[i]
            if total >= threshold:
                ans += 1
            i = k
            while i < len(arr):
                total += arr[i] - arr[i - k]
                if total >= threshold:
                    ans += 1
                i += 1
            return ans
