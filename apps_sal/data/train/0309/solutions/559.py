class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        size = len(A)
        if size <= 1:
            return size
        nums = [{} for _ in range(size)]
        for i in range(1, size):
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff in nums[j]:
                    nums[i][diff] = nums[j][diff] + 1
                else:
                    nums[i][diff] = 2
        max_num = 0
        for i in range(1, size):
            max_num = max(max_num, max(nums[i].values()))
        return max_num
