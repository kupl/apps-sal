class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def combinationSumRecu(self, candidates, target, start, intermediate, result):
            if target == 0:
                result.append(list(intermediate))
            while start < len(candidates) and candidates[start] <= target:
                intermediate.append(candidates[start])
                combinationSumRecu(self, candidates, target - candidates[start], start + 1, intermediate, result)
                start += 1
                intermediate.pop()
                while start > 0 and start < len(candidates) and candidates[start] == candidates[start - 1]:
                    start += 1

        combinationSumRecu(self, sorted(candidates), target, 0, [], result)
        return result
