from collections import defaultdict


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        row = tuple([m] * n)

        def valid(row, i, side):
            return i + side <= len(row) and all(h >= side for h in row[i:i + side])

        dp = defaultdict(int)

        def count(row, i):
            if i >= len(row):
                return 0

            if row in dp:
                return dp[row]

            res = float('inf')
            side = 1
            while valid(row, i, side):
                nrow = list(row)
                for j in range(i, i + side):
                    nrow[j] -= side

                ni = i
                while ni < len(row) and not nrow[ni]:
                    ni += 1

                res = min(res, 1 + count(tuple(nrow), ni))
                side += 1

            dp[row] = res
            return res

        return count(row, 0)
