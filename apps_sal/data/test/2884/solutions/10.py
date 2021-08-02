class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sortedCandidates = sorted(candidates)
        if len(candidates) == 0 or target < sortedCandidates[0]:
            return []
        if target == sortedCandidates[0]:
            return [[sortedCandidates[0]]]
        resultWith0 = self.combinationSum2(sortedCandidates[1:], target - sortedCandidates[0])
        nextIndex = 0
        while nextIndex < len(candidates) and sortedCandidates[nextIndex] == sortedCandidates[0]:
            nextIndex += 1

        resultNo0 = self.combinationSum2(sortedCandidates[nextIndex:], target)

        return [[sortedCandidates[0]] + item for item in resultWith0] + resultNo0
