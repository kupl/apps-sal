class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        index = {0: -1}
        best_till = [float('inf')] * len(arr)
        res = float('inf')
        best = float('inf')
        for (i, val) in enumerate(arr):
            if val - target in index:
                start_of_window = index[val - target]
                length = i - start_of_window
                res = min(res, best_till[start_of_window + 1] + length)
                best = min(best, length)
            if i + 1 < len(best_till):
                best_till[i + 1] = best
            index[val] = i
        return -1 if res == float('inf') else res


'\ntarget=7\n[1,6,1]\n\narr=[1,7,8]\nindex { 0->-1, 1->0, }\nbest_till= [inf, 2, 2]\nres = inf\n\ni=2, val=8\nstart_of_window = 0\nlength = 2\n\n'
