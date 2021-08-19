class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tup_list = sorted(list(zip(difficulty, profit)))
        filtered_list = []
        best = 0
        for (d, p) in tup_list:
            if p > best:
                best = p
                filtered_list.append((d, p))
        worker = sorted(worker)
        profit = 0
        dix = 0
        for w in worker:
            if w < filtered_list[dix][0]:
                continue
            while dix + 1 < len(filtered_list) and filtered_list[dix + 1][0] <= w:
                dix += 1
            profit += filtered_list[dix][1]
        return profit
