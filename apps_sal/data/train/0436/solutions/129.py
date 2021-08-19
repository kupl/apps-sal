class Solution:
    def minDays(self, n: int) -> int:
        #         dp = [0] * (n+1)
        #         # dp[0] = 1

        #         for i in range(1, n + 1):
        #             # print(i, dp[i-1], i - i/2, i - (2*i/3), i%2, i%3)
        #             dp[i] = 1 + min(dp[i-1], 1e9 if i % 2 != 0 else dp[i - int(i/2)], 1e9 if (i % 3 != 0 or i < 2*i/3) else dp[i - int(2*i/3)])

        #         # print(dp)

        #         return dp[n]
        queue = deque([[n, 0]])
        vis = set()

        while(len(queue)):
            curr, days = queue.popleft()
            if curr in vis:
                continue

            if curr == 0:
                return days

            vis.add(curr)

            if curr % 3 == 0:
                queue.append([curr / 3, days + 1])

            if curr % 2 == 0:
                queue.append([curr / 2, days + 1])

            queue.append([curr - 1, days + 1])
