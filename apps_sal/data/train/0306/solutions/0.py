class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cache = {}

        def f(val):
            if val == target:
                return 1

            total = 0
            remain = target - val
            for num in nums:
                if num <= remain:
                    k = val + num
                    if k in cache:
                        total += cache[k]
                    else:
                        cache[k] = f(val + num)
                        total += cache[k]
            return total

        return f(0)
