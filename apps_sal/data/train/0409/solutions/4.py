class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        m = 10**9 + 7

        # kadane helper algo
        def kadane(numbers):
            best = 0
            curr = 0
            for x in numbers:
                curr = max(0, curr + x)
                best = max(best, curr)
            return best

        # stupid approach
        #a = arr*k
        # return max_subarray(a) % m

        tot = sum(arr)

        if not k:
            return 0
        elif k == 1:
            return kadane(arr) % m
        else:
            return ((k - 2) * max(tot, 0) + kadane(arr * 2)) % m
