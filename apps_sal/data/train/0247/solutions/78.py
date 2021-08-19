class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        for (i, cur) in enumerate(arr):
            if cur - target in prefix:
                end = prefix[cur - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[cur] = i
        return -1 if ans == math.inf else ans
