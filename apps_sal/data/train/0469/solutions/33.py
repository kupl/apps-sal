class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        outdegree = [0] * n
        visited = [False] * n

        possible_roots = []
        for i in range(n):
            if leftChild[i] != -1:
                outdegree[i] += 1
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                outdegree[i] += 1
                indegree[rightChild[i]] += 1

        for i in range(n):
            if indegree[i] == 0 and outdegree[i] <= 2:
                possible_roots.append(i)
                # check for more than one root node
                if len(possible_roots) > 1:
                    return False

            if outdegree[i] > 2:
                return False

        if not possible_roots:
            return False

        queue = deque()
        queue.append(possible_roots[0])
        while queue:
            node = queue.popleft()
            if visited[node]:
                return False

            visited[node] = True

            lc = leftChild[node]
            rc = rightChild[node]
            if lc != -1:
                queue.append(lc)
            if rc != -1:
                queue.append(rc)

        return all(visited)
