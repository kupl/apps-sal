class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0

        dp = [0] * len(days)

        # given a day, find the dp index should look for
        # include start, not include end
        def search(start: int, end: int, day: int) -> int:
            if start == end - 1:
                if day >= days[start]:
                    return start
                else:
                    return -1
            m = int((end - start) / 2) + start

            if day >= days[m]:
                return search(m, end, day)
            else:
                return search(start, m, day)

        m = {day: i for i, day in enumerate(days)}

        for i, day in enumerate(days):
            prev_1 = day - 1
            prev_7 = day - 7
            prev_30 = day - 30
            c_1 = costs[0]
            c_7 = costs[1]
            c_30 = costs[2]
            if prev_1 in m:
                c_1 += dp[m[prev_1]]
            elif prev_1 >= 0 and prev_1 >= days[0]:
                c_1 += dp[search(0, i, prev_1)]
            if prev_7 in m:
                c_7 += dp[m[prev_7]]
            elif prev_7 >= 0 and prev_7 >= days[0]:
                c_7 += dp[search(0, i, prev_7)]
            if prev_30 in m:
                c_30 += dp[m[prev_30]]
            elif prev_30 >= 0 and prev_30 >= days[0]:
                c_30 += dp[search(0, i, prev_30)]

            dp[i] = min(c_1, c_7, c_30)

        return dp[-1]
