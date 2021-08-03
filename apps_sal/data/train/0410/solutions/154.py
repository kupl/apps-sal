class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def BFS(queue):
            while queue:
                var, level = queue.popleft()
                if var == 1:
                    return level
                if var % 2:
                    queue.append([3 * var + 1, level + 1])
                else:
                    queue.append([var / 2, level + 1])
        ans = []
        for i in range(lo, hi + 1):
            ans.append((i, BFS(deque([[i, 0]]))))
        ans = sorted(ans, key=lambda l: l[1])
        return ans[k - 1][0]
