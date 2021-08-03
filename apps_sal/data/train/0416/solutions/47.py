class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        dp = {}
        n = len(graph)

        def dfs(im, ic, nmove):
            mouse_move = nmove % 2
            if im == 0:
                return 1
            if im == ic:
                return 2
            if nmove >= 2 * n + 1:
                dp[(im, ic, nmove)] = 0
                return 0
            if (im, ic, nmove) in dp:
                return dp[(im, ic, nmove)]

            wins = [0, 0, 0]
            ret = None
            if mouse_move:
                for nxt in graph[im]:
                    idx = dfs(nxt, ic, nmove + 1)
                    wins[idx] += 1
                    if idx == 1:
                        break
                if wins[1] > 0:
                    ret = 1
                elif wins[0] > 0:
                    ret = 0
                else:
                    ret = 2
            else:
                for nxt in graph[ic]:
                    if nxt != 0:
                        idx = dfs(im, nxt, nmove + 1)
                        wins[idx] += 1
                        if idx == 2:
                            break

                if wins[2] > 0:
                    ret = 2
                elif wins[0] > 0:
                    ret = 0
                else:
                    ret = 1
            dp[(im, ic, nmove)] = ret
            return ret

        res = dfs(1, 2, 1)
        return res
