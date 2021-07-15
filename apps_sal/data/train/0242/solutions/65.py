class Solution:
    def isvalid(self,D):
        if len(D)>2:
            return False
        if len(D)==1:
            a = min(D)
            if a==1 or D[a]==1:
                return True
            return False
        # len(D)==2 now
        a,b = min(D),max(D)
        if a==D[a]==1:
            return True
        return True if (a==(b-1) and D[b]==1) else False
    def maxEqualFreq(self, A):
        best = 0
        B = Counter() # Count number of repetitions/length (per value)
        C = Counter() # Count number of times a length has been seen
        for i,x in enumerate(A):
            if B[x]:
                # If we had seen B before, deregister its \"old\" length
                if C[B[x]] == 1:
                    C.pop( B[x] )
                else:
                    C[B[x]] -= 1
            B[x]    += 1 # increase rep. counter
            C[B[x]] += 1 # Register new length seen
            #
            if self.isvalid(C):
                best = i+1
        return best
