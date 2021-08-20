class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        graph = {}
        indegree = {}
        for w in words:
            graph[w] = []
            indegree[w] = 0

        def is_pre(wd_sml, wd_lrg):
            for idx in range(len(wd_lrg)):
                if wd_lrg[:idx] + wd_lrg[idx + 1:] == wd_sml:
                    return True
            return False
        for idx in range(1, len(words)):
            for idx2 in range(idx):
                if len(words[idx]) != len(words[idx2]) + 1:
                    continue
                if is_pre(words[idx2], words[idx]):
                    graph[words[idx2]].append(words[idx])
                    indegree[words[idx]] += 1
        memo = {}
        from collections import deque

        def dfs(wd):
            if wd in memo:
                return memo[wd]
            res = 1
            for nei in graph[wd]:
                res = max(res, 1 + dfs(nei))
            memo[wd] = res
            return memo[wd]
        st_arr = [w for (w, indeg) in list(indegree.items()) if not indeg]
        max_len = 0
        for elt in st_arr:
            res_len = dfs(elt)
            max_len = max(res_len, max_len)
        return max_len
