class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = {}

        def helper(n, lastnum):
            if n == 0:
                return 1
            if (n, lastnum) in memo:
                return memo[n, lastnum]
            res = 0
            for num in range(6):
                if num == lastnum:
                    continue
                for i in range(1, rollMax[num] + 1):
                    nxtn = n - i
                    if nxtn < 0:
                        break
                    res += helper(nxtn, num)
            memo[n, lastnum] = res % (10 ** 9 + 7)
            return memo[n, lastnum]
        return helper(n, None)
