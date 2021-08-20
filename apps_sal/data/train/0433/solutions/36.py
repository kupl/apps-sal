class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k - 1
        total = sum(arr[0:k])
        if total / k >= threshold:
            count = 1
        else:
            count = 0
        while r < len(arr) - 1:
            total -= arr[l]
            l += 1
            r += 1
            total += arr[r]
            if total / k >= threshold:
                count += 1
        return count
