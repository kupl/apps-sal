class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        (i, j) = (0, k - 1)
        total = sum(arr[i:j + 1])
        target = threshold * k
        res = 0
        if total >= target:
            res += 1
        while j < len(arr) - 1:
            total -= arr[i]
            i += 1
            j += 1
            total += arr[j]
            if total >= target:
                res += 1
        return res
