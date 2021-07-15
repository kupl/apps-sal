class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        
        def make(B):
            ans = [None]*N
            stack = []
            for i in B:
                while stack and i>stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans
                
                
        # sort A[i] in the order of value  
        # B is a list of index
        B = sorted(range(N), key = lambda i:A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)
        
        
        odd = [False]*N
        even = [False]*N
        odd[N-1] = even[N-1] = True
        
        # sort from back to the front dynamic program
        for i in range(N-2, -1, -1):
            if oddnext[i]:
                odd[i] = even[oddnext[i]]
            if evennext[i]:
                even[i] = odd[evennext[i]]
        return sum(odd)
