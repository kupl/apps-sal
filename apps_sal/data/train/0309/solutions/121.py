class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                d = A[j]-A[i]
                dic[j,d]=dic.get((i,d),1)+1
                # if (i,d) in dic:
                #     dic[(j,d)]=dic[(i,d)]+1
                # else:
                #     dic[(j,d)]=2
                
        return max(dic.values())

