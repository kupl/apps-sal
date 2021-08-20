class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        @lru_cache(None)
        def helper(idx):
            ans = 1
            (ub, lb) = (1, 1)
            while ub <= d or lb <= d:
                if idx + ub < len(arr) and arr[idx + ub] < arr[idx]:
                    ans = max(ans, 1 + helper(idx + ub))
                    ub += 1
                else:
                    ub = sys.maxsize
                if idx - lb >= 0 and arr[idx - lb] < arr[idx]:
                    ans = max(ans, 1 + helper(idx - lb))
                    lb += 1
                else:
                    lb = sys.maxsize
            return ans
        return max([helper(idx) for idx in range(len(arr))])
