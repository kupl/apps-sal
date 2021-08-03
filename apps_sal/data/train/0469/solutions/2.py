class Solution:
    def validateBinaryTreeNodes(self, n: int, left_children: List[int], right_children: List[int]) -> bool:

        root = self.find_root(n, left_children, right_children)
        if root == -1:
            return False

        return self.helper(root, n, left_children, right_children)

    def find_root(self, n, left_children, right_children):
        left_counter = collections.Counter(left_children)
        right_counter = collections.Counter(right_children)
        for i in range(n):
            if i not in left_counter and i not in right_counter:
                return i

        return -1

    def helper(self, root, n, left_children, right_children):
        visited = set()
        if not self.dfs(root, left_children, right_children, visited):
            return False

        # print(visited)
        return len(visited) == n

    def dfs(self, root, left_children, right_children, visited):
        if root == -1:
            return True

        if root in visited:
            return False

        visited.add(root)
        left = self.dfs(left_children[root], left_children, right_children, visited)
        right = self.dfs(right_children[root], left_children, right_children, visited)

        return left and right
