class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def isPred(w1, w2):
            if len(w1) + 1 != len(w2):
                return False
            flag = 0

            for i in range(len(w1)):
                if w1[i] != w2[i + flag] and flag == 0:
                    flag = 1
                    if w1[i] != w2[i + flag]:
                        return False
                elif w1[i] != w2[i + flag] and flag != 0:
                    return False
            return True

        def dfs(i):
            if i in memo:
                return memo[i]

            max_level = 0
            for next_i in graph[i]:
                level = dfs(next_i)
                if level > max_level:
                    max_level = level
            memo[i] = max_level + 1
            return memo[i]

        n = len(words)
        if n <= 1:
            return n

        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isPred(words[i], words[j]):
                    graph[i].append(j)
        # graph, time: O(n*n*k), space(n*n*k)
        memo = {}
        ans = 0
        for i in range(n):
            level = dfs(i)
            if level > ans:
                ans = level
        # dfs, time: O(n), space(n)
        return ans
