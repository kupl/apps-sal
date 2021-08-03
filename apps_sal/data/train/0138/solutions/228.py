class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if num == 0:
                dp.append(0)
            elif num > 0:
                dp.append(1)
            else:
                dp.append(-1)
        for i in range(1, len(dp)):
            if dp[i - 1] == 0:
                continue
            else:
                dp[i] *= dp[i - 1]
        print(dp)
        dic = {}
        res = 0
        zero = -1
        for i, num in enumerate(dp):
            if num > 0:
                if 1 not in dic:
                    res = max(res, i - zero)
                    dic[1] = i
                else:
                    res = max(res, i - dic[1] + 1, i - zero)
            elif num == 0:
                dic = {}
                zero = i
            else:
                if -1 not in dic:
                    dic[-1] = i
                else:
                    res = max(res, i - dic[-1])
        return res
