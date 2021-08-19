class Solution:

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def prod(nums):
            prod = 1
            for i in nums:
                prod *= i
            return prod

        def listsplit(ls1, index):
            result = []
            st = -1
            for i in index:
                if i == 0:
                    st = i
                else:
                    result.append(ls1[st + 1:i])
                    st = i
            if st < len(ls1) - 1:
                result.append(ls1[st + 1:])
            return result
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = []
        if 0 in nums:
            zeros = [i for i in range(len(nums)) if nums[i] == 0]
            sublist = listsplit(nums, zeros)
            result.append(0)
        else:
            sublist = [nums]
        sublist = [i for i in sublist if i]
        for i in sublist:
            if prod(i) < 0:
                negative = [j for j in range(len(i)) if i[j] < 0]
                (left, right) = (negative[0], negative[-1])
                if len(i) == 1:
                    result_t = i[0]
                elif left == 0 or right == len(i) - 1:
                    result_t = max(prod(i[left + 1:]), prod(i[:right]))
                else:
                    (left_p, right_p) = (prod(i[:left]), prod(i[right + 1:]))
                    if left_p <= right_p:
                        result_t = prod(i[left + 1:])
                    else:
                        result_t = prod(i[:right])
            else:
                result_t = prod(i)
            result.append(result_t)
        return max(result)
