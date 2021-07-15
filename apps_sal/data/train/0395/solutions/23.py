from sortedcontainers import SortedList

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        dpO = [False] * n
        dpE = [False] * n
        dpO[-1] = dpE[-1] = True
        sl = SortedList()
        sl.add(A[-1])
        indexes = collections.defaultdict(int)
        indexes[A[-1]] = n - 1
        
        for i in range(n - 2, -1, -1):
            num = A[i]
            idx = sl.bisect_left(num)
            if 0 <= idx < len(sl):                
                val_idx = indexes[sl[idx]]
                dpO[i] = dpE[val_idx]
            idx = idx if 0 <= idx < len(sl) and sl[idx] == num else idx - 1
            if 0 <= idx < len(sl):
                val_idx = indexes[sl[idx]]
                dpE[i] = dpO[val_idx]
            sl.add(num)
            indexes[num] = i
            
        return sum(dpO)

