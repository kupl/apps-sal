class Solution:

    def minOperations(self, nums: List[int]) -> int:
        to_ret = 0
        max_len = 0
        for t in nums:
            st = bin(t)[2:]
            max_len = max(max_len, len(st))
            to_ret += sum(map(int, st))
        return to_ret + max_len - 1
