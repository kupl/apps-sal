class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        #
        # DP ----- 544 ms (25.55%) / 19 MB (27.94%)
        # Only consider three cases: residue is in [0, 1, 2]
        # Maintain the greatest sum with residue [0, 1, 2] divived by 3, respectively.
        # For each number, consider the result when adding it and check whether the sum increases or not.
        # ------------------------------------------------------------------------------------------------------------
        dic = {0: 0}

        for n in nums:
            dic_new = {}
            #  If add `n`, the temporary result is denoted by `dic_new`
            for i, s in dic.items():
                r = (i + n) % 3
                dic_new[r] = max(n + s, dic.get(r, 0))
            # Update `dict` by `dic_new`
            for i, s in dic_new.items():
                dic[i] = max(s, dic.get(i, 0))

        return dic.get(0, 0)
