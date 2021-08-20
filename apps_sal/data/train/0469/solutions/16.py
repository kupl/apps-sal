class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        edge = [[] for i in range(n)]
        cntEdge = 0
        for (u, v) in enumerate(leftChild):
            if v == -1:
                continue
            else:
                edge[u].append(v)
                edge[v].append(u)
                cntEdge += 1
        for (u, v) in enumerate(rightChild):
            if v == -1:
                continue
            else:
                edge[u].append(v)
                edge[v].append(u)
                cntEdge += 1
        if cntEdge != n - 1:
            return False
        vis = [False for i in range(n)]
        stack = []
        stack.append(0)
        while stack:
            u = stack.pop()
            vis[u] = True
            for v in edge[u]:
                if not vis[v]:
                    stack.append(v)
        return all(vis)
