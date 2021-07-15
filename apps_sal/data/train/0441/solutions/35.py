class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 1
        cur_iter = 1
        while True:
            N -= cur_iter
            res = N / (cur_iter+1)
            if res < 1:
                break
            if res.is_integer():
                ans += 1
            cur_iter += 1
        return ans

