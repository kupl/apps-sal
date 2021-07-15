class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        parent = [i for i in range(N)]
        rank = [0] * N
        size = [1] * N
        groupCount = Counter()
        visited = set()
        ans = -1
        
        for i, num in enumerate(arr, 1):
            num -= 1
            visited.add(num)
            groupCount[1] += 1
            
            if num - 1 in visited:
                self.union(parent, rank, size, groupCount, num, num - 1)
                
            if num + 1 in visited:
                self.union(parent, rank, size, groupCount, num, num + 1)
                
            if groupCount[m] > 0:
                ans = i
                
        return ans
            
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])

        return parent[x]

    def union(self, parent, rank, size, groupCount, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)
        groupCount[size[xRoot]] -= 1
        groupCount[size[yRoot]] -= 1
        size[xRoot] = size[yRoot] = size[xRoot] + size[yRoot]
        groupCount[size[xRoot]] += 1

        if rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        elif rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1
