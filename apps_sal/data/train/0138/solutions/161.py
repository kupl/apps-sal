class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start_neg = -1
        end_neg = -1
        start_idx = -1
        end_idx = -1
        acc_product = None
        ans = 0
        nums += [0]
        for idx, num in enumerate(nums):
            if num == 0:
                if start_idx == -1:
                    continue
                if acc_product > 0:
                    ans = max(ans, end_idx - start_idx + 1)
                else:
                    if start_neg - start_idx < end_idx - end_neg:
                        ans = max(ans, end_idx - start_neg - 1 + 1)
                    else:
                        ans = max(ans, end_neg - start_idx - 1 + 1)
                start_idx = -1
                end_idx = -1
                acc_product = None
                start_neg = -1
                end_neg = -1
            else:
                if start_idx < 0:
                    start_idx = idx
                end_idx = idx
                if not acc_product:
                    acc_product = 1
                acc_product *= num
                if num < 0:
                    end_neg = idx
                    if start_neg < 0:
                        start_neg = idx

        return ans
