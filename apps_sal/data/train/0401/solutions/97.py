class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dic = {0: 0}

        for n in nums:
            dic_new = {}

            for i, s in dic.items():
                r = (i + n) % 3
                dic_new[r] = max(n + s, dic.get(r, 0))

            for i, s in dic_new.items():
                dic[i] = max(s, dic.get(i, 0))

        return dic.get(0, 0)
