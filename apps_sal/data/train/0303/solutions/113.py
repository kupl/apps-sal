class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        mem = {}
        
        def find(s, e):
            if (s,e) in mem:
                return mem[(s,e)]
            
            if e-s == 1:
                return arr[s]
            elif e-s == 0:
                return 0
            else:
                m = None
                for i in range(s+1, min(s+k+1, len(arr)+1)):
                    subsum = max(arr[s:i])*(i-s) + find(i,e)
                    if m is None or subsum > m:
                        m = subsum
                mem[(s,e)] = m
                return m
            
        return find(0, len(arr))
