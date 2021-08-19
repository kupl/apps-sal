class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0] * len(arr)
        path = {i: [(i, arr[i])] for i in range(len(arr))}

        def jump(i):
            nonlocal dp, path
            if dp[i] != 0:
                return dp[i]
            left, right = 0, 0
            nl, nr = i, i
            for j in range(i + 1, i + d + 1):
                if j >= len(arr):
                    break
                if arr[j] < arr[i]:
                    t = jump(j)
                    if right < t:
                        right = t
                        nr = j
                else:
                    break
            for j in range(i - 1, i - d - 1, -1):
                if j < 0:
                    break
                if arr[j] < arr[i]:
                    t = jump(j)
                    if left < t:
                        left = t
                        nl = j
                else:
                    break
            if left < right and right > 0:
                path[i] += path[nr]
            elif left >= right and left > 0:
                path[i] += path[nl]
            dp[i] = max(left, right) + 1
            return dp[i]

        ans = 0
        for i in range(len(arr)):
            jump(i)
            # print(i, path[i])
            ans = max(ans, dp[i])
        return ans
