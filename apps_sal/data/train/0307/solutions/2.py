class Solution:
    def soupServings(self, N: int) -> float:
        seen={}
        def find_prob(A,B):
            if A==0 and B==0:
                return 0.5
            if A==0:
                return 1
            if B==0:
                return 0
            if (A,B) in seen:
                return seen[A,B]
            temp=0
            for x,y in [[100,0],[75,25],[50,50],[25,75]]:
                temp+=find_prob(A-x if A>x else 0,B-y if B>y else 0)
            seen[A,B]=0.25*temp
            return 0.25*temp
        if N>4800: return 1.0
        return find_prob(N,N)
