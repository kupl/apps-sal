class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        idxes = range(N)
        
        def make(B):
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    pop = stack.pop()
                    ans[pop] = i
                stack.append(i)
            return ans
        
        sorted_idxes = sorted(idxes, key=lambda i: A[i])
        oddnext = make(sorted_idxes)
        sorted_idxes_rev = sorted(idxes, key=lambda i: -A[i])
        evennext = make(sorted_idxes_rev)
        
        odd = [False] * N
        even = [False] * N
        
        odd[N-1] = True
        even[N-1] = True
        
        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        #print(odd, even)
            
        #print(A, sorted_idxes, sorted_idxes_rev)
        return sum(1 for x in odd if x)
