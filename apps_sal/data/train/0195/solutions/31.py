class Solution:
    def countTriplets(self, A: List[int]) -> int:
        umap = collections.Counter(A)
        n = len(A)
        mask = (1 << 16) - 1
        
        for i in range(n):
            for j in range(i+1, n):
                key = A[i] & A[j]
                if key not in umap:
                    umap[key] = 0
                umap[key] += 2
        
        result = 0
        for a in A:
            d = (~a) & mask
            key = d
            result += umap.get(d, 0)
            while d > 0:
                d = (d-1)&key
                result += umap.get(d, 0)
        return result

