class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        prefix = {0: -1}
        best_till = [math.inf] * len(arr)
        ans = best = math.inf

        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:

                # j is on the left
                # i is on the right
                j = prefix[curr - target]

                if j > -1:
                    # Update the ans, the current one and the non-overlapping best one
                    ans = min(ans, i - j + best_till[j])

                # update the shortest length until i
                best = min(best, i - j)

            best_till[i] = best
            prefix[curr] = i

        return -1 if ans == math.inf else ans
