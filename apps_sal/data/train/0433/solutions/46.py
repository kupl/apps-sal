class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        s = sum(arr[:k - 1])
        t = threshold * k
        for i in range(k - 1, len(arr)):
            s += arr[i]
            if s >= t:
                res += 1
            s -= arr[i + 1 - k]
        return res
