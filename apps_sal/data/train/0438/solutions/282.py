class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        size = [0] * (len(arr) + 2)
        count = collections.defaultdict(int)
        
        answer = -1
        for i, value in enumerate(arr):
            left, right = size[value - 1], size[value + 1]
            size[value] = size[value - left] = size[value + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[size[value]] += 1
            
            if count[m]:
                answer = i + 1
        
        return answer
        
    def findLatestStep_my(self, arr: List[int], m: int) -> int:
        parent = [0] * (len(arr) + 2)
        size = [1] * (len(arr) + 1)
        
        count = collections.defaultdict(int)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                count[size[py]] -= 1
                count[size[px]] -= 1
                size[py] += size[px]
                count[size[py]] += 1
        
        answer = -1
        for i, value in enumerate(arr):
            parent[value] = value
            count[1] += 1
            
            if parent[value - 1]:
                union(value - 1, value)
            if parent[value + 1]:
                union(value, value + 1)
            
            if count[m]:
                answer = i + 1
        
        return answer
