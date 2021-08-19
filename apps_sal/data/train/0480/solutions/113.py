class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        rec = [1]
        mod = 10**9 + 7

        for i in range(1, steps + 1):
            temp = []
            for j in range(min(i + 1, arrLen)):
                temp.append(sum(rec[max(0, j - 1): min(j + 2, arrLen)]) % mod)
            rec = temp
#            print(rec)
        return rec[0]
