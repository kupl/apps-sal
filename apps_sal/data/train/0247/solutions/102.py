class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        mapsum = {}
        mapsum[0] = -1
        totsum = 0

        best_till = [math.inf] * len(arr)
        best = math.inf
        end = -1
        res = float('inf')

        for i in range(len(arr)):
            totsum += arr[i]
            if (totsum - target) in mapsum:
                end = mapsum[totsum - target]
                if end > -1:
                    res = min(res, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            mapsum[totsum] = i

        if res < math.inf:
            return res
        return res if res < math.inf else -1
