class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)

        def get_val(nums):
            if len(nums) == 0:
                return 0
            products = [1]
            product = 1
            length = len(nums)
            for i in range(length):
                product *= nums[i]
                products.append(product)
            for j in range(length, 0, -1):
                for k in range(length - j + 1):
                    value = products[k + j] // products[k]
                    if value > 0:
                        return j
            return 0
        index = 0
        maximum = 0
        for i in range(n):
            if nums[i] == 0:
                if i == index:
                    index += 1
                    continue
                value = get_val(nums[index:i])
                if value > maximum:
                    maximum = value
                index = i + 1
            elif nums[i] > 0:
                nums[i] = 1
            else:
                nums[i] = -1
        value = get_val(nums[index:n])
        if value > maximum:
            maximum = value
        return maximum
