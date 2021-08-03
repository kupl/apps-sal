import bisect


class Solution:
    def solve(self, diff, profit, worker):
        mp = {}
        for i in range(len(diff)):
            d = diff[i]
            p = profit[i]
            if d not in mp:
                mp[d] = 0
            mp[d] = max(mp[d], p)
        diff2 = sorted(mp.keys())
        ln = len(diff2)
        mx = [0] * ln
        for i in range(ln):
            d = diff2[i]
            p = mp[d]
            if i == 0:
                mx[i] = p
            else:
                mx[i] = max(mx[i - 1], p)
        total = 0
        # print(diff2)
        # print(profit2)
        # print(mx)
        # print('---')
        for w in worker:
            if w < diff2[0]:
                continue
            i = bisect.bisect_left(diff2, w)
            if i >= len(diff2):
                i = len(diff2) - 1
            elif diff2[i] > w:
                i -= 1
                if i < 0:
                    continue
            max_profit = mx[i]
            # print(w, i, mx[i])
            total += max_profit
        return total

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        return self.solve(difficulty, profit, worker)
