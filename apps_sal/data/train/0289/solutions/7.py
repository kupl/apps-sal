class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        tl = sum(A[:L])
        ll = [tl]
        for i in range(L,len(A)):
            tl-=A[i-L]
            tl+=A[i]
            ll.append(tl)
        print(ll)
        tl = sum(A[:M])
        ml = [tl]
        for i in range(M,len(A)):
            tl-=A[i-M]
            tl+=A[i]
            ml.append(tl)
        print(ml)
        maxx = 0
        for i in range(len(ll)):
            for j in range(len(ml)):
                if i+L-1<j or j+M-1<i:
                    maxx = max(maxx, ll[i]+ml[j])
        return maxx
