def build_graph(n, leftChild, rightChild):
    adj_list = [[] for _ in range(n)]
    for i in range(len(leftChild)):
        left = leftChild[i]
        right = rightChild[i]
        if left != -1:
            adj_list[i].append(left)
        if right != -1:
            adj_list[i].append(right)
    return adj_list


def gather_inDegrees(n, graph):
    inDegrees = [0] * n
    for i in range(len(graph)):
        for neighbor in graph[i]:
            inDegrees[neighbor] += 1
    return inDegrees


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = build_graph(n, leftChild, rightChild)
        inDegrees = gather_inDegrees(n, graph)
        print(inDegrees)
        zero_count = 0
        for count in inDegrees:
            if count > 1:
                return False
            if count == 0:
                if zero_count == 1:
                    return False
                else:
                    zero_count += 1

        visited = set()
        topo_order = []
        processing = set()

        def _dfs(node):
            processing.add(node)
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor in visited and neighbor in processing:
                    return True
                else:
                    if neighbor not in visited:
                        if _dfs(neighbor):
                            return True
            processing.remove(node)
            topo_order.append(node)
            return False

        for i in range(n):
            if i not in visited:
                if _dfs(i):
                    return False
        return True
