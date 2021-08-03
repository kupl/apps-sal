class Solution:

    @staticmethod
    def process(st, end, cnt_neg, arr):
        if st >= 0 and st <= end and end >= 0:
            if not (cnt_neg % 2):
                return end - st + 1
            first_neg_ind = st
            last_neg_ind = end
            while(first_neg_ind <= end and arr[first_neg_ind] >= 0):
                first_neg_ind += 1
            while(last_neg_ind >= st and arr[last_neg_ind] >= 0):
                last_neg_ind -= 1
            print((st, end, first_neg_ind, last_neg_ind))
            return max(last_neg_ind - st, end - first_neg_ind)

        return 0

    def getMaxLen(self, nums: List[int]) -> int:
        prev = 0
        ans = 0
        cnt_neg = 0
        for i in range(len(nums)):
            if not nums[i]:
                ans = max(ans, Solution.process(prev, i - 1, cnt_neg, nums))
                prev = i + 1
                cnt_neg = 0
            if nums[i] < 0:
                cnt_neg += 1
        ans = max(ans, Solution.process(prev, len(nums) - 1, cnt_neg, nums))
        return ans
