class Solution:
    def knightDialer(self, N: int) -> int:
        dp = {}
        MOD = 10**9 + 7

        def moveOnce(num0, N0):
            if (num0, N0) in dp:
                return dp[(num0, N0)]
            if N0 == 0:
                return 1
            if N0 < 0:
                return 0
            subAns = 0
            if num0 == 1:
                subAns = moveOnce(6, N0 - 1) + moveOnce(8, N0 - 1)
            elif num0 == 2:
                subAns = moveOnce(7, N0 - 1) + moveOnce(9, N0 - 1)
            elif num0 == 3:
                subAns = moveOnce(4, N0 - 1) + moveOnce(8, N0 - 1)
            elif num0 == 4:
                subAns = moveOnce(3, N0 - 1) + moveOnce(9, N0 - 1) + moveOnce(0, N0 - 1)
            elif num0 == 5:
                subAns = 0  # moveOnce(5, N0-2) + moveOnce(7, N0-2) + moveOnce(9, N0-2)
            elif num0 == 6:
                subAns = moveOnce(1, N0 - 1) + moveOnce(7, N0 - 1) + moveOnce(0, N0 - 1)
            elif num0 == 7:
                subAns = moveOnce(2, N0 - 1) + moveOnce(6, N0 - 1)  # + moveOnce(5, N0-2) + moveOnce(7, N0-2)
            elif num0 == 8:
                subAns = moveOnce(1, N0 - 1) + moveOnce(3, N0 - 1)
            elif num0 == 9:
                subAns = moveOnce(2, N0 - 1) + moveOnce(4, N0 - 1)  # + moveOnce(5, N0-2) + moveOnce(9, N0-2)
            elif num0 == 0:
                subAns = moveOnce(4, N0 - 1) + moveOnce(6, N0 - 1)
            dp[(num0, N0)] = subAns % MOD
            return subAns
        return sum([moveOnce(i, N - 1) for i in range(10)]) % MOD
