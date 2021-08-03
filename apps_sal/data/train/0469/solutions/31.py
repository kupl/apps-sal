class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        unvisited = set([i for i in range(n)])

        graph = defaultdict(set)

        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                graph[i].add(leftChild[i])

        for i in range(len(rightChild)):
            if rightChild[i] != -1:
                graph[i].add(rightChild[i])

        zero_indegree_nodes = set(unvisited)

        for k, v in graph.items():
            for node in v:
                if node in zero_indegree_nodes:
                    zero_indegree_nodes.remove(node)

        if len(zero_indegree_nodes) != 1:
            return False

        def visit(node):
            unvisited.remove(node)

            for nbr in graph[node]:
                if nbr not in unvisited:
                    return True
                if visit(nbr):
                    return True

            return False

        x = visit(list(zero_indegree_nodes)[0])

        if x == True:
            return False

        if len(unvisited) > 0:
            return False

        return True
