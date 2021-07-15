class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        l= 0 
        summ = 0
        A.insert(0,0)
        ln = len(A)
        for i in range(1,ln):
            A[i]+=A[i-1]
        minq = collections.deque([0])
        best = float('inf')
        for r in range(1,ln):
            while minq and A[r]-A[minq[0]]>=K:
                best = min(best,r-minq[0])
                minq.popleft()
            while minq and A[minq[-1]]>A[r]:
                minq.pop()
            minq.append(r)
        return best if best!=float('inf') else -1
