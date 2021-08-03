class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        maxim = max(nums)

        total = 0
        for k in range(len(nums)):
            num_div = 0

            index = 2
            div = []
            curr_val = nums[k]
            if abs(int(sqrt(curr_val)) - sqrt(curr_val)) > 10**(-12):
                while index <= int(sqrt(curr_val)):

                    if curr_val % index == 0:
                        div.append(index)

                        div.append(nums[k] / index)
                    if len(div) > 2:
                        break
                    index += 1

                if len(div) == 2:
                    total = total + sum(div) + 1 + nums[k]

        return int(total)
