class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        arr = []
        for d, p in sorted(zip(difficulty, profit)):
            if arr and arr[-1][1] >= p:
                continue
            arr.append([d, p])

        N = len(arr)
        res, i, best = 0, 0, 0
        for w in sorted(worker):
            while i < N and w >= arr[i][0]:
                best = arr[i][1]
                i += 1

            res += best
        return res
