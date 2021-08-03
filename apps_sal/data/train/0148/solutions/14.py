class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        l = sorted(zip(profit, difficulty), reverse=True)

        worker.sort(reverse=True)

        p = 0

        for w in worker:
            while l and w < l[0][1]:
                l.pop(0)
            if not l:
                break
            p += l[0][0]
        return p
