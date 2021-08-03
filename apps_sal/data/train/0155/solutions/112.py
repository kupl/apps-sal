class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        ans = dict()

        def dfs(idx):
            if idx in ans:
                return
            ans[idx] = 1

            i = idx - 1
            while i >= 0 and idx - i <= d and arr[i] < arr[idx]:
                dfs(i)
                ans[idx] = max(ans[idx], ans[i] + 1)
                i -= 1

            i = idx + 1
            while i < len(arr) and i - idx <= d and arr[i] < arr[idx]:
                dfs(i)
                ans[idx] = max(ans[idx], ans[i] + 1)
                i += 1

        for i in range(len(arr)):
            dfs(i)
        print(ans)
        return max(ans.values())
