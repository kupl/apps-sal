class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)

        @lru_cache(None)
        def rec(idx):
            if not 0 <= idx < N:
                return -inf
            ans = 1
            for i in range(idx - 1, idx - d - 1, -1):
                if i < 0 or arr[i] >= arr[idx]:
                    break
                ans = max(ans, rec(i) + 1)

            for i in range(idx + 1, idx + d + 1):
                if i >= N or arr[i] >= arr[idx]:
                    break
                ans = max(ans, rec(i) + 1)

            return ans

        ans = 0
        for i in range(N):
            ans = max(ans, rec(i))

        return ans
