class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        i = 0
        prefixSum = 0
        existed = {0: 0}
        res = 0
        while i <= len(hours) - 1:
            if hours[i] >= 9:
                prefixSum += 1
            else:
                prefixSum -= 1
            if prefixSum not in existed:
                existed[prefixSum] = i + 1
            if prefixSum - 1 in existed:
                res = max(res, i + 1 - existed[prefixSum - 1])
            if prefixSum >= 1:
                res = max(res, i + 1)
            i += 1
        return res
