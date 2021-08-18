class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()

        quotient = []
        remainder = []
        ret = 0

        for num in nums:
            quotient.append(num // 3 * 3)
            remainder.append(num % 3)
            ret += num

        remainder_sum = ret % 3
        if remainder_sum == 0:
            return ret
        elif remainder_sum == 1:
            remainder1 = 0
            remainder1_count = 0
            remainder2 = 0
            remainder2_count = 0
            for i in range(len(nums)):
                if remainder[i] == 1:
                    if remainder1_count >= 1:
                        continue
                    remainder1_count += 1
                    remainder1 += nums[i]
                if remainder[i] == 2:
                    if remainder2_count >= 2:
                        continue
                    remainder2_count += 1
                    remainder2 += nums[i]
                if remainder2_count >= 1 and remainder1_count >= 2:
                    break

            if remainder2_count == 2 and remainder1_count == 1:
                return ret - min(remainder1, remainder2)
            elif remainder2_count == 2:
                return ret - remainder2
            elif remainder1_count == 1:
                return ret - remainder1
            else:
                return 0
        else:
            remainder1 = 0
            remainder1_count = 0
            remainder2 = 0
            remainder2_count = 0
            for i in range(len(nums)):
                if remainder[i] == 1:
                    if remainder1_count >= 2:
                        continue
                    remainder1_count += 1
                    remainder1 += nums[i]
                if remainder[i] == 2:
                    if remainder2_count >= 1:
                        continue
                    remainder2_count += 1
                    remainder2 += nums[i]
                if remainder2_count >= 1 and remainder1_count >= 2:
                    break

            if remainder2_count == 1 and remainder1_count == 2:
                return ret - min(remainder1, remainder2)
            elif remainder2_count == 1:
                return ret - remainder2
            elif remainder1_count == 2:
                return ret - remainder1
            else:
                return 0

            return 0

        return 0
