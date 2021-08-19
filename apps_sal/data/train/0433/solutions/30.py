class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = l = 0
        for r in range(k):
            s += arr[r]
        ans = 0
        while r < len(arr) - 1:
            if s >= threshold * k:
                ans += 1
            s -= arr[l]
            l += 1
            r += 1
            s += arr[r]
        ans += s >= threshold * k
        return ans
