class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        count = arr[0] % 2
        currentCount = count
        for i in range(1, len(arr)):
            if arr[i] % 2 == 1:
                currentCount = i - currentCount + 1
            count += currentCount
        return count % (10 ** 9 + 7)
