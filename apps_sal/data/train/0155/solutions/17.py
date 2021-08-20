class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        ans = [1] * len(arr)

        def dp(i):
            nonlocal ans, arr, d
            if ans[i] != 1:
                return ans[i]
            for dr in [-1, 1]:
                for k in range(i, i + d * dr + dr, dr):
                    if k < 0 or k == i:
                        continue
                    if k > len(arr) - 1 or arr[k] >= arr[i]:
                        break
                    ans[i] = max(ans[i], 1 + dp(k))
            return ans[i]
        for i in range(len(arr)):
            dp(i)
        return max(ans)
