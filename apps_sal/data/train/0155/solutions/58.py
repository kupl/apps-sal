class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        hp = [(v, i) for (i, v) in enumerate(arr)]
        heapq.heapify(hp)
        dp = [0] * len(arr)
        res = 0
        while hp:
            (h, i) = heapq.heappop(hp)
            tmp = 1
            for j in range(i - 1, i - 1 - d, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                tmp = max(tmp, dp[j] + 1)
            for j in range(i + 1, i + 1 + d):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                tmp = max(tmp, dp[j] + 1)
            dp[i] = tmp
        return max(dp)
