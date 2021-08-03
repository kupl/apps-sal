class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pref = {0: -1}

        result = best = math.inf
        best_till = [math.inf] * len(arr)

        for i, curr in enumerate(itertools.accumulate(arr)):
            diff = curr - target
            if diff in pref:
                left = pref[diff]
                length = i - left
                result = min(result, best_till[left] + length)
                best = min(best, length)

            pref[curr] = i
            best_till[i] = best
        return result if result < math.inf else -1
