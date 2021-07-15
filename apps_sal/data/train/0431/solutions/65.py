class Solution:

    def next_smallest(self, A):
        
        inds = [-1]*len(A)

        stack = []

        for i, val in enumerate(A):

            while len(stack)>0 and A[stack[-1]]>val:
                inds[stack[-1]] = i
                stack.pop()

            stack+=[i]
            
        return inds

    def last_smallest(self, A):

        inds = [-1]*len(A)

        stack = []

        for i, val in reversed(list(enumerate(A))):

            while len(stack)>0 and A[stack[-1]]>=val:
                inds[stack[-1]] = i
                stack.pop()

            stack+=[i]
            
        return inds
        

    def sumSubarrayMins(self, A):

        left = self.last_smallest(A)
        right = self.next_smallest(A)

        tot = 0

        n = len(A)

        for i, val in enumerate(A):
            
            p = left[i]
            q = right[i]

            a = i-p
            b = q-i

            if p==-1:
                a = i+1

            if q==-1:
                b = n-i

            nseqs = a*b

            tot+=nseqs*val

        return tot % (10**9+7)

