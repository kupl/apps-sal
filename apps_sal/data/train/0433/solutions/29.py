class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        temp = sum(arr[:k])
        count = 0 if temp / k < threshold else 1
        for i in range(k, len(arr)):
            temp = temp - arr[i - k] + arr[i]
            if temp / k >= threshold:
                count += 1
        return count
