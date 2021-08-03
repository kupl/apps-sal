class Solution(object):
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        return -1 if ans == math.inf else ans

    def OldminSumOfLengths(self, arr, target):
        ans, l = math.inf, len(arr)
        la = [math.inf] * l

        p1, p2, s, ml = 0, 0, arr[0], math.inf
        while p1 < l and p2 < l:
            action = None
            la[p2] = ml
            curl = p2 - p1 + 1
            if s == target:
                ml = min(ml, curl)
                la[p2] = ml
                if p1 - 1 >= 0:
                    ans = min(ans, la[p1 - 1] + curl)
                p2 += 1
                action = 1
            elif s < target:
                p2 += 1
                action = 1
            elif s > target:
                p1 += 1
                action = -1
            if p1 >= l or p2 >= l:
                break
            elif p1 > p2:
                p2 = p1
                s = arr[p1]
            else:
                if action == 1:
                    s += arr[p2]
                elif action == -1:
                    s -= arr[p1 - 1]
        return -1 if ans == math.inf else ans
