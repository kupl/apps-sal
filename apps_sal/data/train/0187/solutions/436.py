class Solution:

    def minOperationsMaxProfit(self, A: List[int], profit: int, loss: int, wait=0, total=0, best=0, bestIndex=-1) -> int:
        i = 1

        def rotate():
            nonlocal i, wait, total, best, bestIndex
            take = min(wait, 4)
            total += take
            wait -= take
            cand = total * profit - i * loss
            if best < cand:
                best = cand
                bestIndex = i
            i += 1
        for x in A:
            wait += x
            rotate()
        while wait:
            rotate()
        return bestIndex
