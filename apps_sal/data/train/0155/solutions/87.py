class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # dp
        n = len(arr)
        res = [0] * n
        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i+di, i+d*di+di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max(map(dp, range(n)))
