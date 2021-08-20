class Solution:

    def getMaxLenDuh(self, nums: List[int]) -> int:
        """
        Single pass: at each num, track length of pos and neg prods:
            reset on 0, and change sign as needed.
        """
        size = len(nums)
        if not size:
            return 0
        if size == 1:
            return 1 if nums[0] > 0 else 0
        result = nneg = npos = 0
        for num in nums:
            if num == 0:
                nneg = npos = 0
            elif num > 0:
                npos = npos + 1
                nneg = nneg + 1 if nneg else 0
            else:
                temp = nneg
                nneg = npos + 1
                npos = temp + 1 if temp else 0
            result = max(result, npos)
        return result

    def getMaxLenPow2(self, numso: List[int]) -> int:
        """

        """
        nums = [copysign(num, 2) for num in numso]
        size = len(nums)
        if size == 0:
            return
        (left_prod, right_prod) = (0, 0)
        max_prod = -float('inf')
        for i in range(size):
            left_prod = (left_prod or 1) * nums[i]
            right_prod = (right_prod or 1) * nums[size - 1 - i]
            max_prod = max(max_prod, left_prod, right_prod)
        return math.log(max_prod, 2)

    def getMaxLen(self, nums: List[int]) -> int:
        """

        """
        return self.getMaxLenDuh(nums)
