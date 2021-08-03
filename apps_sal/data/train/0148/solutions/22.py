class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        value = list(zip(difficulty, profit))
        value.sort()
        print(value)
        res = 0
        i = 0
        best = 0
        for person in sorted(worker):
            while i < len(value) and person >= value[i][0]:
                best = max(best, value[i][1])
                i += 1
            res += best

        return res
