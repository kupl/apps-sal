class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        nums += [0]
        max_so_far = 0
        N = len(nums)
        res = 1
        (last_zero, last_neg, first_neg, last_pos) = (0, -1, N, -1)
        for i in range(N):
            res *= nums[i]
            if nums[i] == 0:
                if res > 0:
                    max_so_far = max(max_so_far, i - last_zero + 1)
                else:
                    max_so_far = max(max_so_far, i - first_neg, last_pos - last_zero + 1)
                last_zero = i + 1
                first_neg = N
                last_pos = last_zero if i < N - 1 and nums[i + 1] > 0 else last_zero - 1
                res = 1
            elif nums[i] < 0 and first_neg == N:
                first_neg = i + 1
            elif res > 0:
                last_pos = i
        return max_so_far
