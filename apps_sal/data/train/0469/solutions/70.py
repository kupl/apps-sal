class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = collections.defaultdict(list)
        edges = 0
        indegree = [0]*n
        for i in range(n):
            if leftChild[i] >= 0:
                graph[i].append(leftChild[i])
                indegree[leftChild[i]] += 1
                edges += 1
            if rightChild[i] >= 0:
                graph[i].append(rightChild[i])
                indegree[rightChild[i]] += 1
                edges += 1
        
        if edges != n-1:
            return False
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        if len(q) != 1:
            return False
        
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.pop()
                n -= 1
                for nei in graph[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        
        return n == 0

