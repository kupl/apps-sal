class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = []
        for n in arr:
            if len(prefix) == 0:
                prefix.append(n)
            else:
                prefix.append(prefix[-1] + n)
        indexMap = {}
        indexMap[0] = -1
        best = output = float('inf')
        best_till = [float('inf')] * len(arr)
        for (i, p) in enumerate(prefix):
            if p - target in indexMap:
                output = min(output, i - indexMap[p - target] + best_till[indexMap[p - target]])
                best = min(best, i - indexMap[p - target])
            best_till[i] = best
            indexMap[p] = i
        return -1 if output == float('inf') else output
