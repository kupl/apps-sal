
class Solution:
    def maxNonOverlapping(self, arr: List[int], target: int) -> int:
        prevSums, n = {0: -1}, len(arr)
        prefixSum, count, lastIndex = 0, 0, -1

        for i in range(n):
            prefixSum += arr[i]
            rem = prefixSum - target
            if rem in prevSums and prevSums[rem] >= lastIndex:
                count += 1
                lastIndex = i
            prevSums[prefixSum] = i
        return count
