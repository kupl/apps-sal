class Solution:

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def produce(nums, target, current, output):
            if target == 0:
                output.append(list(current))
                return
            for (i, n) in enumerate(nums):
                if n > target:
                    continue
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                current.append(n)
                produce(nums[i + 1:], target - n, current, output)
                current.pop()
        output = []
        candidates.sort()
        produce(candidates, target, [], output)
        return output
