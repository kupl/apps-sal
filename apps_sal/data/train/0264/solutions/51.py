class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def valid(w):
            return all(v <= 1 for v in collections.Counter(w).values())

        def dfs(i, cand):
            if i < 0:
                return 0
            res = dfs(i - 1, cand)
            if valid(arr[i]) and all(c in cand for c in arr[i]):
                new_cand = {c for c in cand if c not in collections.Counter(arr[i]).keys()}
                res = max(res, dfs(i - 1, new_cand) + len(arr[i]))

            return res

        return dfs(len(arr) - 1, {chr(i + ord('a')) for i in range(26)})
