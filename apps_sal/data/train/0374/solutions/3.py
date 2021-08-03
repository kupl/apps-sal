# https://zxi.mytechroad.com/blog/searching/leetcode-943-find-the-shortest-superstring/
# 将每个单词看作是一个节点, 两两之间有一条带有权重的有向路径, 权重表示为
# g[i][j]: the cost of appending word[j] after word[i]
# 如将 gcta 放在 catg 后面的 cost 为 3 因为它们有公共子串 g, 所以总长度只需要再增加 3
# 问题转化为了在一个有向图里, 从任意点出发找到经过所有点各一次的最短路径
# dp[s][i]: min cost to visit nodes of s and ends with i (s is a binary string)
# dp[14][2] is the min cost of visit nodes 1, 2, 3 and ends with 2 (14 = 2^1 + 2^2 + 2^3)
# 初始化 dp[2^i][i] = len(A[i]), visit A[i] cost len(A[i])
# dp[s][i] = min(dp[s - 2^i][j] + g[j][i]), 找到所有的没有经过节点 i 的状态, 然后将 i 接在 j 后面
# 结果是 min(dp[2^n - 1][*]), 遍历完了所有的点 (2^n - 1) 的最小 cost
# 用 parent[2^i][i] 数组存储节点 i 的父节点, 以便回溯得到最终的字符串
# O(n^2 * 2^n) time complexity, O(n * 2^n) space complexity
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        def dist(s1, s2):
            ans = 0
            for k in range(min(len(s1), len(s2))):
                if s1[len(s1) - k:] == s2[:k]:
                    ans = len(s2) - k
            return ans

        n = len(A)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                g[i][j] = dist(A[i], A[j])
                g[j][i] = dist(A[j], A[i])

        parent = [[-1] * n for _ in range(1 << n)]
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(A[i])  # 初始化每个节点是第一个点的情况

        for s in range(1, 1 << n):
            for i in range(n):
                if not (s & (1 << i)):  # 以点 i 作为结尾则状态 s 必须已经访问过 i, 所以 s 的第 i 位是 1
                    continue
                prev = s - (1 << i)  # 找到上一个状态
                for j in range(n):  # 对于所有点, 尝试让它们作为上一个点
                    if dp[prev][j] + g[j][i] < dp[s][i]:
                        dp[s][i] = dp[prev][j] + g[j][i]
                        parent[s][i] = j

        end = dp[-1].index(min(dp[-1]))  # 找到遍历完所有点后的最小 cost 的最终节点
        s = (1 << n) - 1  # 最终的状态
        res = ''
        while s:
            prev = parent[s][end]
            if prev < 0:  # 初始化 parent 为 -1, 小于 0 说明这个节点没有父节点
                res = A[end] + res
            else:
                res = A[end][len(A[end]) - g[prev][end]:] + res
            s &= ~ (1 << end)  # 上一个状态
            end = prev
        return res
