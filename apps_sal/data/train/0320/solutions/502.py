class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0   # minus 1
        maxLen = 0   # divided by 2
        for num in nums:
            num_bin = bin(num)[2:]
            cnt += sum(map(int, num_bin))
            maxLen = max(maxLen, len(num_bin))
        return cnt + maxLen - 1
