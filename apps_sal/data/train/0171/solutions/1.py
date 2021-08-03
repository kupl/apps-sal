class Solution:

    def maxProduct(self, nums):
        self._prod_cache = {}
        m_value = None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            a_value = self.get_max_prod(nums, i, 1)
            if m_value is None or a_value > m_value:
                m_value = a_value
        return m_value

    def get_max_prod(self, nums, i, acc_p):
        if i < 0:
            return None
        if (i, acc_p) in self._prod_cache:
            return self._prod_cache[(i, acc_p)]
        val = nums[i]
        if i > 0:
            max_p = max(self.get_max_prod(nums, i - 1, acc_p * val),
                        acc_p * val)
        else:
            max_p = acc_p * val

        self._prod_cache[(i, acc_p)] = max_p
        return max_p
