class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)

        if n < 3:
            return n

        max_count = 0

        dp = [[set(), 0, set(), 0] for _ in range(n)]

        dp[0] = [{tree[0]}, 1, {tree[0]}, 1]

        for i in range(1, n):
            if tree[i] in dp[i - 1][2]:
                set_2 = dp[i - 1][2].copy()
                count_2 = dp[i - 1][3] + 1
            else:
                temp = dp[i - 1][0].copy()
                temp.add(tree[i])
                set_2 = temp
                count_2 = dp[i - 1][1] + 1
            if tree[i] in dp[i - 1][0]:
                set_1 = dp[i - 1][0].copy()
                count_1 = dp[i - 1][1] + 1
            else:
                set_1 = {tree[i]}
                count_1 = 1

            dp[i] = [set_1, count_1, set_2, count_2]

            max_count = max(max_count, max(count_1, count_2))

        return max_count
