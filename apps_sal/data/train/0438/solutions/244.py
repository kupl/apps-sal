class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        parents = list(range(N))
        sizes = [0] * N
        
        islands = set()
        
        def union(one, two):
            r1 = findroot(one)
            r2 = findroot(two)
            
            if r1 == r2: return sizes[r1]
            if sizes[r1] == m and r1 in islands:
                islands.remove(r1)
            if sizes[r2] == m and r2 in islands:
                islands.remove(r2)
            big, small = (r1, r2) if sizes[r1] > sizes[r2] else (r2, r1)
            parents[small] = big
            sizes[big] += sizes[small]
            return sizes[big]
        
        def findroot(pos):
            if parents[pos] != pos:
                parents[pos] = findroot(parents[pos])
            return parents[pos]
        
        last_round = -1
        for i, pos in enumerate(arr, 1):
            pos -= 1
            sizes[pos] += 1
            sz = sizes[pos]
            if pos < N - 1 and sizes[pos + 1]:
                sz = union(pos, pos+1)
            if pos > 0 and sizes[pos - 1]:
                sz = union(pos-1, pos)
            if sz == m:
                islands.add(findroot(pos))
            if islands:
                last_round = i
        
        return last_round
            

