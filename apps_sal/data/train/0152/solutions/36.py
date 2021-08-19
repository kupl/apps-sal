class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #         def pd(i, m):
        #             if m == 1:
        #                 return float(\"inf\")

        #             if memo[i][m]:
        #                 return memo[i][m]

        #             res = 0

        #             for j in range(i+1, len(position)):
        #                 res = max(res, min(position[j] - position[i], pd(j, m-1)))

        #             memo[i][m] = res

        #             return res

        #         position = sorted(position)

        #         memo = [(1 + m) * [0] for _ in range(1 + len(position))]

        #         res = pd(0, m)

        position = sorted(position)

        if m == 2:
            return position[-1] - position[0]

        def solve(threshold, m):
            last_ball_pos = position[0]

            for pos in position[1:]:
                if pos - last_ball_pos >= threshold:
                    m -= 1
                    last_ball_pos = pos

                if m == 0:
                    return True

            return False

        start = 0
        end = position[-1] - position[0]

        res = 0

        while start <= end:
            middle = (start + end) // 2

            if solve(middle, m - 1):
                start = middle + 1
                res = max(res, middle)

            else:
                end = middle - 1

        return res
