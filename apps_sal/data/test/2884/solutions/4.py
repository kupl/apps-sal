class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(L, target, path, ans):
            if target == 0:
                ans.append(path)
                return
            for i in range(len(L)):
                if L[i] > target:
                    return
                if i > 0 and L[i] == L[i - 1]:
                    continue
                helper(L[i + 1:], target - L[i], path + [L[i]], ans)

        ans = []
        helper(sorted(candidates), target, [], ans)
        return ans
