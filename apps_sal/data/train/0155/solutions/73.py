class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            left, right = i, i
            max_range = 1
            while left - 1 >= 0 and arr[left - 1] < arr[i] and left - 1 >= i - d:
                left -= 1
            while right + 1 < n and arr[right + 1] < arr[i] and right + 1 <= i + d:
                right += 1

            for nxt in range(left, right + 1):
                if nxt != i:
                    max_range = max(max_range, 1 + dfs(nxt))

            return max_range

        return max(dfs(i) for i in range(n))
