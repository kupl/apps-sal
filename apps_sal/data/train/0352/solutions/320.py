class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        adj = {}
        for w in words:
            for i in range(len(w)):
                s = w[0:i] + w[i + 1:]
                if s not in adj:
                    adj[s] = [w]
                else:
                    adj[s].append(w)
        res = 1
        queue = []
        visited = {}

        def dfs(root):
            if root in visited:
                return visited[root]
            if root not in adj:
                visited[root] = 1
                return 1
            distance = 1
            for next_ in adj[root]:
                distance = max(distance, dfs(next_) + 1)
            visited[root] = distance
            return distance
        for w in words:
            length = dfs(w)
            res = max(res, length)
        return res
