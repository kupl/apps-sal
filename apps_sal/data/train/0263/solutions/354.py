class Solution:
    def knightDialer(self, N: 'int') -> 'int':
        path_graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        mem = {}
        if N == 1:
            return 10

        def dfs(n, steps):
            if steps == 1:
                return len(path_graph[n])
            if (n, steps) not in mem:
                all_paths = 0
                for next_num in path_graph[n]:
                    all_paths += dfs(next_num, steps - 1)
                mem[(n, steps)] = all_paths
            return mem[(n, steps)]
        result = 0
        for n in range(10):
            temp = dfs(n, N - 1)
            result += temp
        return result % (10**9 + 7)
