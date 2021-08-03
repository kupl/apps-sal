class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def bfs(n):
            if n not in self.remainingNodes:
                self.isValid = False
                return
            self.remainingNodes.remove(n)
            if len(nodes[n]) > 2:
                self.isValid = False
                return
            for child in nodes[n]:
                if child != -1 and child not in self.remainingNodes:
                    self.isValid = False
                    return
                if child != -1:
                    bfs(child)

        def findRoot():
            if len(leftChild) == 1:
                if leftChild[0] == rightChild[0] == -1:
                    return 0
            for node in parents:
                for parent in parents[node]:
                    if parent not in parents:
                        return parent

        nodes = collections.defaultdict(list)
        parents = collections.defaultdict(list)

        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                nodes[i].append(leftChild[i])
                parents[leftChild[i]].append(i)
            if rightChild[i] != -1:
                nodes[i].append(rightChild[i])
                parents[rightChild[i]].append(i)

        self.isValid = True
        self.remainingNodes = set(i for i in range(n))
        root = findRoot()
        bfs(root)
        return self.isValid and not self.remainingNodes
