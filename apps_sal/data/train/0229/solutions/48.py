from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c=Counter(A)
        A=sorted(A)
        for num,v in sorted(list(c.items()), key= lambda item:item[0]):
            if num>0 and c[num]>0:
                if c[num]!=0 and c[num]>c[2*num]:
                    return False
                c[2*num]-=c[num]
                c[num]=0
            elif num<0 and c[num]>0:
                if num%2==1:
                    return False
                if c[num]!=0 and c[num]>c[num//2]:
                    return False
                c[num//2]-=c[num]
                c[num]=0
        return True
            

