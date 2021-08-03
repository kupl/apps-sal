class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        cur = 0
        ans = 0
        for i in range(len(arr)):
            cur += arr[i]
            if i >= k:
                cur -= arr[i - k]
            if i >= k - 1 and cur >= k * t:
                ans += 1
        return ans
