class Solution:

    def validateBinaryTreeNodes(self, nodes: int, leftChild: List[int], rightChild: List[int]) -> bool:
        num_edges = 0
        graph = collections.defaultdict(list)
        indegree = {i: 0 for i in range(nodes)}
        parents = {i: None for i in range(nodes)}
        for (n, (l, r)) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                num_edges += 1
                graph[n].append(l)
                if parents[l] is not None or parents[n] == l:
                    return False
                parents[l] = n
                indegree[l] += 1
            if r != -1:
                num_edges += 1
                graph[n].append(r)
                if parents[r] is not None or parents[n] == r:
                    return False
                parents[r] = n
                indegree[r] += 1
        if num_edges != nodes - 1:
            return False
        roots = [i for i in range(len(parents)) if parents[i] is None]
        if len(roots) != 1:
            return False
        root = roots[0]
        return max(leftChild[root], rightChild[root]) != -1 or nodes == 1
