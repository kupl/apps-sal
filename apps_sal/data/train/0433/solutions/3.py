class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minVal = k * threshold

        beg = 0
        end = k - 1
        total = 0
        currSum = 0

        for i in range(beg, end + 1):
            currSum += arr[i]

        while end < len(arr):
            if beg != 0:
                currSum = currSum - arr[beg - 1] + arr[end]

            if currSum >= minVal:
                total += 1
            beg += 1
            end += 1

        return total
