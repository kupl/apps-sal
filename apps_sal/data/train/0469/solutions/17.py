class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [False] * n
        cycle = False

        def dfs(root):
            nonlocal cycle
            if root == -1:
                return
            if not visited[root]:
                visited[root] = True
                dfs(leftChild[root])
                dfs(rightChild[root])
            else:
                cycle = True

        def find_root():
            in_degree = {}
            for i in range(n):
                in_degree[i] = 0
            in_degree[-1] = 0
            for i in range(n):
                in_degree[leftChild[i]] += 1
                in_degree[rightChild[i]] += 1
            has_seen = False
            root = None
            print(in_degree)
            for (k, v) in list(in_degree.items()):
                if v == 0:
                    if has_seen:
                        return None
                    root = k
                    has_seen = True
            return root
        root = find_root()
        print(root)
        if root == None:
            return False
        dfs(root)
        if cycle:
            return False
        return all(visited)
