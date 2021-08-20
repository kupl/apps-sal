class Solution:

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtracing(nums, target, idx, path, ret):
            if not target:
                if path not in ret:
                    ret.append(path)
            for i in range(idx, len(nums)):
                if nums[i] > target:
                    break
                backtracing(nums, target - nums[i], i + 1, path + [nums[i]], ret)
        candidates.sort()
        ret = []
        backtracing(candidates, target, 0, [], ret)
        return ret
