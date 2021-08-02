class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(candidates, k, target, res, result):
            for i in range(k, len(candidates)):
                if target == candidates[i]:
                    temp = [j for j in res]
                    temp.append(candidates[i])
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                    return
                elif target < candidates[i]:
                    return
                else:
                    res.append(candidates[i])
                    combination(candidates, i + 1, target - candidates[i], res, result)
                    res.pop()

        candidates.sort()
        res = []
        result = []
        combination(candidates, 0, target, res, result)
        return(result)
