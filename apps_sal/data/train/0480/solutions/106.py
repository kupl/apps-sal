class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps + 1, arrLen)
        ans = [0] * arrLen
        ans[0] = 1
        for i in range(steps):
            new_ans = []
            for j in range(arrLen):
                tmp = ans[j]
                if j > 0:
                    tmp += ans[j - 1]
                if j < arrLen - 1:
                    tmp += ans[j + 1]
                new_ans.append(tmp)
            ans = new_ans
        return ans[0] % (10**9 + 7)
