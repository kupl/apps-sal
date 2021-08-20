class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ls = sorted(range(len(difficulty)), key=lambda x: difficulty[x])
        workers = sorted(worker)
        idx = 0
        resp = 0
        best = 0
        for worker in workers:
            while idx < len(ls) and worker >= difficulty[ls[idx]]:
                best = max(best, profit[ls[idx]])
                idx += 1
            resp += best
        return resp
