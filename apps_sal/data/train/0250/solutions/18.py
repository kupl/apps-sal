class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:

        # 计算最低工资/工作质量的比值；用一个堆维护K个工作质量最低的工作人员

        workers = []

        for q, w in zip(quality, wage):

            workers.append((w / q, q, w))

        workers.sort()

        ans = float('inf')
        dui = []
        sumq = 0

        for ratio, q, w in workers:
            # 最小堆变为最大堆
            heapq.heappush(dui, -q)
            sumq += q

            if len(dui) > K:
                # 去掉一个最高的quality
                sumq = sumq + heapq.heappop(dui)

            if len(dui) == K:
                ans = min(ans, ratio * sumq)

        return ans
