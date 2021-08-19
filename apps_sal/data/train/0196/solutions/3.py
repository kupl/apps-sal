class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        mini = maxi = A[0]
        curMin = curMax = total = 0
        for num in A:
            curMin = min(curMin + num, num)  # 2
            curMax = max(curMax + num, num)  # 7
            maxi = max(maxi, curMax)  # 7
            mini = min(mini, curMin)  # -3
            total += num
        return max(maxi, total - mini) if maxi > 0 else maxi
