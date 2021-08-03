# Jenny 20201002
# sample 180 ms submission

# 857. Minimum Cost to Hire K Workers

import heapq


class Solution:
    # time O(nlogn), space O(n)
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # 团队开销= 最低效人的 w/q * 团队总 q
        # 开除当前团队最低效的人
        # 引进待选集合中quality最小的人。
        workers = sorted((w / q, w, q) for w, q in zip(wage, quality))
        ans = float('inf')
        pool = []
        sum_q = 0

        for (ratio, w, q) in workers:
            heapq.heappush(pool, -q)
            sum_q += q

            if len(pool) > K:
                sum_q += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sum_q)

            # print(sum_q, ans)
        return float(ans)
