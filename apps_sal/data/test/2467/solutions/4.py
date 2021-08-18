class Solution:
    result = []

    def combinationSum3Util(self, candidates, current_subset, k, target, start):
        if target == 0 and k == 0:
            Solution.result.append(current_subset)

        elif target != 0 and k != 0:
            for i in range(start, len(candidates)):
                current_candidate_num = candidates[i]
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if target - current_candidate_num >= 0:
                    next_subset = current_subset.copy()
                    next_subset.append(current_candidate_num)
                    self.combinationSum3Util(candidates, next_subset, k - 1, target - current_candidate_num, i + 1)
                else:
                    return

        else:
            return

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        Solution.result = []

        if k == 0:
            return [[]]

        candidates = [x for x in range(1, 10)]
        current_subset = []
        self.combinationSum3Util(candidates, current_subset, k, n, 0)
        return Solution.result
