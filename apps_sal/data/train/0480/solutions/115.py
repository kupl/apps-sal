class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 0 or arrLen == 1:
            return 1

        MODULO = 10 ** 9 + 7
        ans = [0] * arrLen
        ans[0] = 1
        ans[1] = 1

        arrLen = min(steps + 1, arrLen)
        for _ in range(1, steps):
            next_ans = [0] * arrLen
            for j in range(arrLen):
                if j == 0:
                    next_ans[j] = (ans[j] + ans[j + 1]) % MODULO
                elif j == arrLen - 1:
                    next_ans[j] = (ans[j - 1] + ans[j]) % MODULO
                else:
                    next_ans[j] = (ans[j - 1] + ans[j] + ans[j + 1]) % MODULO
            ans = next_ans
        return ans[0]
