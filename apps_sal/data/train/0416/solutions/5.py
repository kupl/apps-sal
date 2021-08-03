class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # state: [M=0/C=1, Mpos, Cpos]
        # result: 0-draw, 1-mouse win, 2-cat win

        cache = {}

        def dfs(s, visited):
            if s in cache:
                return cache[s]
            visited.add(s)
            if s[0] == 0:
                ret = dfs_m(s, visited)
            else:
                ret = dfs_c(s, visited)
            visited.remove(s)
            cache[s] = ret
            return ret

        def sorted_neighbor(node, dest):
            nbs = sorted([(n, dist_mat[n][dest]) for n in graph[node]], key=lambda x: x[1])
            return [t[0] for t in nbs]

        def dfs_m(s, visited):
            if 0 in graph[s[1]]:
                return 1  # mouse-win

            cat_nbs = set([x for x in graph[s[2]] if x != 0])
            nbs = sorted_neighbor(s[1], 0)
            hold_move = 0
            for node in nbs:
                if node == s[2] or node in cat_nbs:  # mouse-lose
                    continue

                s2 = (1, node, s[2])
                if s2 in visited:
                    hold_move += 1
                    continue

                ret = dfs(s2, visited)
                if ret == 1:
                    return 1  # mouse-win
                if ret == 0:
                    hold_move += 1

            if hold_move:
                return 0  # draw
            else:
                return 2  # cat-win

        def dfs_c(s, visited):
            if s[1] in graph[s[2]]:
                return 2  # cat-win

            nbs = sorted_neighbor(s[2], s[1])
            hold_move = 0
            for node in nbs:
                if node == 0:
                    continue

                s2 = (0, s[1], node)
                if s2 in visited:
                    hold_move += 1
                    continue
                ret = dfs(s2, visited)
                if ret == 2:
                    return 2  # cat-win
                if ret == 0:
                    hold_move += 1

            if hold_move:
                return 0  # draw
            else:
                return 1  # mouse-win

        INF_DIST = float('inf')

        def floyd_dist_modified():
            N = len(graph)
            Mat = [[float('inf')] * N for _ in range(N)]
            for i in range(N):
                Mat[i][i] = 0
                for n in graph[i]:
                    Mat[i][n] = 1

            for k in range(1, N):
                for i in range(1, N):
                    for j in range(1, N):
                        Mat[i][j] = min(Mat[i][j], Mat[i][k] + Mat[k][j])

            for n in graph[0]:
                for i in range(1, N):
                    Mat[0][i] = min(Mat[0][i], Mat[0][n] + Mat[n][i])
                    Mat[i][0] = Mat[0][i]

            return Mat

        dist_mat = floyd_dist_modified()
        visited = set()
        return dfs((0, 1, 2), visited)
