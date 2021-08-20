class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = collections.defaultdict(list)
        st = []
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                j = st.pop()
                if i - j <= d:
                    graph[j].append(i)
            st.append(i)
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                j = st.pop()
                if j - i <= d:
                    graph[j].append(i)
            st.append(i)
        visited = {}

        def dfs(i):
            if i in visited:
                return visited[i]
            step = 1
            for j in graph[i]:
                step = max(step, 1 + dfs(j))
            visited[i] = step
            return step
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res
