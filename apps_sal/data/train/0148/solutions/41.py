class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m = len(difficulty)

        difficulty, profit = zip(*sorted(zip(difficulty, profit)))

        difficulty = list(difficulty)
        profit = list(profit)

        best_profit = m * [0]
        best_profit[0] = profit[0]
        ind = 0
        prev_v = difficulty[0]

        for i in range(1, m):
            if prev_v != difficulty[i]:
                ind += 1
                difficulty[ind] = prev_v = difficulty[i]
                best_profit[ind] = best_profit[ind - 1]

            best_profit[ind] = max(best_profit[ind], profit[i])

        m = ind + 1

        def bins(target):
            start = 0
            end = m - 1
            bsres = 0

            while start <= end:
                middle = start + (end - start) // 2

                if difficulty[middle] == target:
                    return best_profit[middle]

                if difficulty[middle] < target:
                    bsres = best_profit[middle]
                    start = middle + 1

                else:
                    end = middle - 1

            return bsres

        res = 0
        h = dict()

        for w in worker:
            if w not in h:
                h[w] = bins(w)

            res += h[w]

        return res
