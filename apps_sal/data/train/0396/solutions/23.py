class Solution:

    def smallestRepunitDivByK(self, k: int) -> int:
        x = k % 10
        if x == 1 or x == 3 or x == 7 or (x == 9):
            cnt = 0
            n = k
            while n > 0:
                n = n // 10
                cnt += 1
            res = 1
            for i in range(cnt - 1):
                res = res * 10 + 1
            while res % k != 0:
                res = res * 10 + 1
                cnt += 1
            return cnt
        else:
            return -1
