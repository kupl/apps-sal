class Solution:
    def isvalid(self,D):
        if len(D)==1:
            a = min(D)
            if a==1 or D[a]==1:
                # a==1: all lengths are unitary (like [1,2,3,4,...]), so removing anything is fine
                # D[a]==1, we have a unique length occurence (like [4,4,4,4,...]), so...
                #          so we can pop one element and be fine
                return True
            return False
        # len(D)==2 now
        a,b = min(D),max(D)
        if a==D[a]==1: 
            # If we remove from a chain of length \"a\", we will create something smaller than \"b\", so...
            # The only way to be fine is to have a single element, like [1,2,2,2,3,3,3,...]
            #     - If we have more of the smallest length, we're into trouble
            return True
        # Remove from \"b\"
        return True if ( D[b]==1 and (a+1)==b ) else False
    def maxEqualFreq(self, A):
        best = 0
        B = Counter() # Count number of repetitions/length (per value)
        C = Counter() # Count number of times a length has been seen
        for i,x in enumerate(A):
            old = B[x]
            if old:
                if C[old]==1:
                    C.pop(old)
                else:
                    C[old] -= 1
            B[x]    += 1 # increase rep. counter
            C[B[x]] += 1 # Register new length seen
            #
            if len(C)<=2 and self.isvalid(C):
                best = i+1
        return best
