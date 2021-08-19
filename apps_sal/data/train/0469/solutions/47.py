class Node:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        (all_nodes, root_nodes) = self.gen_graph(leftChild, rightChild)
        if len(root_nodes) != 1:
            return False
        visited = {all_nodes[root_nodes[0]]}

        def dfs(node):
            if node.left and node.left in visited:
                return False
            if node.right and node.right in visited:
                return False
            if node.left:
                visited.add(node.left)
                if not dfs(node.left):
                    return False
            if node.right:
                visited.add(node.right)
                if not dfs(node.right):
                    return False
            return True
        if not dfs(all_nodes[root_nodes[0]]):
            return False
        for i in range(len(leftChild)):
            if all_nodes[i] not in visited:
                return False
        return True

    def gen_graph(self, left_child, right_child):
        nodes = defaultdict(lambda: Node())
        indegrees = defaultdict(int)
        for i in range(len(left_child)):
            node = nodes[i]
            if left_child[i] != -1:
                node.left = nodes[left_child[i]]
                indegrees[left_child[i]] += 1
            if right_child[i] != -1:
                node.right = nodes[right_child[i]]
                indegrees[right_child[i]] += 1
        root_nodes = [i for i in range(len(left_child)) if indegrees[i] == 0]
        return (nodes, root_nodes)
