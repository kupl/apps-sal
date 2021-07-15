class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        parent = {}
        size = {}
        sizes = collections.defaultdict(int)
        
        def union(a, b):
            fa, fb = find(a), find(b)
            parent[fa] = fb
            sizes[size[fa]] -= 1
            sizes[size[fb]] -= 1
            size[fb] += size[fa]
            sizes[size[fb]] += 1
            
        def get_size(a):
            return size[find(a)]
            
        def find(a):
            if a not in parent:
                parent[a] = a
                size[a] = 1
                sizes[1] += 1
                return parent[a]
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        bits = [0] * len(arr)
        res = -1
        for i, n in enumerate(arr):
            idx = n-1
            bits[idx] = 1
            if idx - 1 >= 0 and bits[idx-1] == 1:
                union(idx, idx-1)
            if idx + 1 < len(bits) and bits[idx + 1] == 1:
                union(idx, idx+1)
            sz = get_size(idx)
            if sizes[m] > 0:
                res = i + 1
        return res
            
    
    
    
    def findLatestStep1(self, arr: List[int], m: int) -> int:
        res, n = -1, len(arr)
        length, cnts = [0] * (n+2), [0] * (n+1)
        for i in range(n):
            a = arr[i]
            left, right = length[a-1], length[a+1]
            newlen = left + right + 1
            length[a] = newlen
            length[a - left] = newlen
            length[a + right] = newlen
            cnts[left] -= 1
            cnts[right] -= 1
            cnts[length[a]] += 1
            if cnts[m] > 0:
                res = i + 1
        return res
