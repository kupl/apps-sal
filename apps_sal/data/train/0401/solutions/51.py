class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        cur = [0] + [-1] * 2
        tmp = cur[:]
        for x in nums:
            for i in range(3):
                idx = (i + x) % 3
                if cur[i] >= 0:
                    tmp[idx] = max(cur[i] + x, cur[idx])

            cur = tmp[:]
        return cur[0]
