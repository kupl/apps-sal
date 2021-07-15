from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ls=[]
        for i in range(31):
            num=2**i
            ls.append(dict(Counter(str(num))))
        # print(ls)
        
        s=str(n)
        di=dict(Counter(s))
        # print(di)
        
        for i in ls:
            if(i==di):
                return True
        return False
