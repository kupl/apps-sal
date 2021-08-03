class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        @lru_cache(None)
        def dfs(i):
            if i == 0 and i + 1 < len(arr):
                if arr[i] <= arr[i + 1]:
                    return 1
            elif i == len(arr) - 1 and i - 1 >= 0:
                if arr[i] <= arr[i - 1]:
                    return 1
            elif i - 1 >= 0 and i + 1 < len(arr) and arr[i] <= arr[i - 1] and arr[i] <= arr[i + 1]:
                return 1

            left_step = 1
            for j in range(i + 1, i + d + 1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                left_step = max(left_step, 1 + dfs(j))
            right_step = 1
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                right_step = max(right_step, 1 + dfs(j))
            return max(left_step, right_step)

        max_step = 0
        for i in range(len(arr)):
            max_step = max(max_step, dfs(i))
            # print(dfs(i))
        return max_step


#         d限定了可能跳的最大步长
#         在步长范围内，跳的距离必须满足中间不能有大于自己的值
#         返回可能到达的最多的下标

#         每个位置有自己可能调到的最多下标
#         比如6-->4
#         14-》8-》6 或者14-》6-》4
#         长度为1000
#         按照高度大小，求解初始跳的步长
#         最终一定是跳到一个山谷或者两端的位置
#         dp[i]: 当位置到达下标i时，可能跳到的最多下标，对于山谷或者两端位置而言，初始值为1
