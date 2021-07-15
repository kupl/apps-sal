class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        rel = zip(difficulty, profit)
        rel = sorted(rel)
        output = 0
        worker.sort()
        mx = 0
        j = 0
        for i in worker:
            while j < len(rel) and i >= rel[j][0]:
                mx = max(mx, rel[j][1])
                j += 1
            print(i, mx)
            output += mx
        return output
