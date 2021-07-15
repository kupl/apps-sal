class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res,curr,prevp,prevn = 0,1,0,None
        
        for i,num in enumerate(nums,1):
            if num==0:
                curr,prevp,prevn = 1,i,None
            else:
                curr*=num
                #print(curr,i,prevp,prevn)
                if curr>0:
                    res = max(res,i-prevp)
                else:
                    if prevn==None:
                        prevn = i
                    else:
                        res = max(res,i-prevn)
        return res

