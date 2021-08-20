from bisect import bisect_right


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = [(d, p) for (d, p) in zip(difficulty, profit)]
        dp.sort()
        G = []
        C = []
        for (x, y) in dp:
            if not G or G[-1] < x:
                G.append(x)
                C.append(y)
                continue
            if G[-1] == x:
                C[-1] = y
        for y in range(1, len(C)):
            if C[y - 1] > C[y]:
                C[y] = C[y - 1]
        ans = 0
        for w in worker:
            idx = bisect_right(G, w) - 1
            if idx >= 0:
                ans += C[idx]
        return ans
