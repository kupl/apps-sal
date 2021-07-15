class Solution:     
    def maxEqualFreq(self, A):
        count = collections.Counter()
        freq = [0 for _ in range(len(A) + 1)]
        res = 0
        for n, a in enumerate(A, 1):
            freq[count[a]]-=1
            freq[count[a]+1]+=1
            c = count[a]=count[a]+1
            if freq[c]*c==n and n<len(A):
                res = n+1
            d = n-freq[c]*c
            if d in [c+1,1] and freq[d]==1:
                res = n
        return res

            


