class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        
        nextSmallestLarger = [-1] * N
        indexes = sorted(range(N), key=lambda i: A[i])
        stk = []
        for i in indexes:
            while stk and i > stk[-1]:
                nextSmallestLarger[stk.pop()] = i
            stk.append(i)
        
        nextLargestSmaller = [-1] * N
        indexes = sorted(range(N), key=lambda i: -A[i])
        stk = []
        for i in indexes:
            while stk and i > stk[-1]:
                nextLargestSmaller[stk.pop()] = i
            stk.append(i)
        
        @lru_cache(None)
        def jump(i, odd):
            if i >= N - 1:
                return True
            
            if odd:
                return False if nextSmallestLarger[i] == -1 else jump(nextSmallestLarger[i], False)
            else:
                return False if nextLargestSmaller[i] == -1 else jump(nextLargestSmaller[i], True)
            
        return sum(jump(i, True) for i in range(N))
