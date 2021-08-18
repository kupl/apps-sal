class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = sum(arr[:k])
        ans = 1 if curr >= threshold * k else 0
        for i in range(k, len(arr)):
            curr += arr[i]
            curr -= arr[i - k]
            if curr >= threshold * k:
                ans += 1
        return ans
