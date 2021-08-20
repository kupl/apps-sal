class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curr_sum = sum(arr[:k])
        res = 1 if curr_sum >= target else 0
        for i in range(k, len(arr)):
            curr_sum = curr_sum - arr[i - k] + arr[i]
            if curr_sum >= target:
                res += 1
        return res
