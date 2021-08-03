class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        result = 0
        for i in range(k, len(arr) + 1):
            avg = total / k
            if avg >= threshold:
                result += 1

            if i < len(arr):
                left = arr[i - k]
                right = arr[i]
                total -= left
                total += right

        return result
