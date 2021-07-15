class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = [set() for _ in range(n)] 
        degree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].add(leftChild[i])
                degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].add(rightChild[i])
                degree[rightChild[i]] += 1
        q = collections.deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
            if degree[i] > 1:
                return False
        if len(q) > 1 or len(q) == 0: return False      
        visited = set()
        while q:
            node = q.pop()
            visited.add(node)
            for neigh in graph[node]:
                if neigh in visited:
                    return False
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    q.append(neigh)
        return len(visited) == n
            

