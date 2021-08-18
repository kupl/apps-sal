class Solution:
    def knightDialer(self, n: int) -> int:

        cell2jump = dict()
        cell2jump[1] = [6, 8]
        cell2jump[2] = [7, 9]
        cell2jump[3] = [4, 8]
        cell2jump[4] = [3, 9, 0]
        cell2jump[5] = []
        cell2jump[6] = [1, 7, 0]
        cell2jump[7] = [2, 6]
        cell2jump[8] = [1, 3]
        cell2jump[9] = [2, 4]
        cell2jump[0] = [4, 6]

        dp = defaultdict()

        def helper(num_jumps, cell):
            if num_jumps == 1:
                return 1
            elif num_jumps == 2:
                return len(cell2jump[cell])

            if (num_jumps, cell) in dp:
                return dp[num_jumps, cell]

            res = 0
            for nei in cell2jump[cell]:
                res += helper(num_jumps - 1, nei)

            dp[num_jumps, cell] = res
            return res

        total = []
        for i in range(10):
            total.append(helper(n, i))

        return sum(total) % (10**9 + 7)
