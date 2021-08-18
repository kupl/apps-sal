import bisect
import heapq


class Solution:
    def minSumOfLengths(self, arr, target):
        lo = 0
        hi = 0
        cur = arr[0]

        pairs = []

        running_min = []

        ans = 1e9

        while lo <= hi and hi < len(arr):
            if cur >= target:
                if cur == target:
                    best_range = hi - lo + 1
                    if len(running_min):
                        best_range = min(best_range, running_min[-1][1])
                        prev_index = bisect.bisect(running_min, (lo, -1)) - 1
                        if 0 <= prev_index < len(running_min):
                            ans = min(ans, hi - lo + 1 + running_min[prev_index][1])

                    running_min.append((hi, best_range))
                    heapq.heappush(pairs, (hi, lo))

                cur -= arr[lo]
                lo += 1
                if hi < lo:
                    hi = lo
                else:
                    continue
            else:
                hi += 1

            if hi < len(arr):
                cur += arr[hi]

        return ans if ans != 1e9 else -1
