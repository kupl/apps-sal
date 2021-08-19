class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        end = k
        count = 0
        sumInit = sum(arr[start:end])
        if sumInit / k >= threshold:
            count += 1
        while end < len(arr):
            sumInit = sumInit - arr[start] + arr[end]
            if sumInit / k >= threshold:
                count += 1
            start += 1
            end += 1
        return count
