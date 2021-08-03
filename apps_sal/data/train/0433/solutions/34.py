class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        temp = 0
        for i in range(l, r + 1):
            temp += arr[i]
        res = 0 if temp < k * threshold else 1
        while r < len(arr) - 1:
            temp += arr[r + 1] - arr[l]
            r += 1
            l += 1
            if temp >= k * threshold:
                res += 1
        return res
