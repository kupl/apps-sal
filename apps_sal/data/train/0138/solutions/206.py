class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        m=0
        neg=0
        pos=0
        positiveBeforeFirstNeg=0
        pos2=0
        for i in nums:
            if(i==0):
                if(neg>0 and neg%2!=0):
                    neg-=1
                if(positiveBeforeFirstNeg<pos2 and neg>2):
                    pos-=positiveBeforeFirstNeg
                    pos+=pos2
                m=max(max(pos,pos2)+neg,m)
                neg,pos,pos2=0,0,0
            elif(i<0):
                if(neg==0):
                    positiveBeforeFirstNeg=pos
                neg+=1
                if(neg%2==0):
                    pos+=pos2
                    pos2=0
            else:
                if(neg%2!=0):
                    pos2+=1
                else:
                    pos+=1
        if(positiveBeforeFirstNeg<pos2 and neg>2):
            pos-=positiveBeforeFirstNeg
            pos+=pos2
        if(neg>0 and neg%2!=0):
            neg-=1
        m=max(max(pos,pos2)+neg,m)     
        return m
