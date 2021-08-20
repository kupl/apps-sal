class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total % 3 == 0:
            return total
        nums_set = set(nums)
        nums.sort()
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        (div, mod) = divmod(total, 3)
        while mod <= total:
            if mod in nums_set:
                return div * 3
            for i in range(n - 2):
                sum_val = 0
                if nums[i] > mod:
                    break
                for j in range(i + 1, n - 1):
                    if nums[i] + nums[j] == mod:
                        return div * 3
                    for k in range(j + 1, n):
                        sum_val += prefix_sum[k] - prefix_sum[i - 1]
                        if sum_val == mod:
                            return div * 3
                        if sum_val > mod:
                            break
            div -= 1
            mod += 3
