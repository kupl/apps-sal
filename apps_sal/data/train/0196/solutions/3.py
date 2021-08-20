class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mini = maxi = A[0]
        curMin = curMax = total = 0
        for num in A:
            curMin = min(curMin + num, num)
            curMax = max(curMax + num, num)
            maxi = max(maxi, curMax)
            mini = min(mini, curMin)
            total += num
        return max(maxi, total - mini) if maxi > 0 else maxi
