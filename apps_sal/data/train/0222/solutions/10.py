class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index_dict={}
        for index,item in enumerate(A):
            index_dict[item]=index
        longest=collections.defaultdict(lambda:2)
        
        res=0
        for index,value in enumerate(A):
            for j in range(index):
                i=index_dict.get(value-A[j],None)
                if(i is not None and i<j):
                    longest[j,index]=longest[i,j]+1
                    res=max(longest[j,index],res)
        if(res<3):
            res=0
        return res 

