class Solution:

    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        lst={1:0}
        num_list=[]
        for i in range(lo,hi+1):
            ans=0
            while i!=1:
                if i in list(lst.keys()):
                    ans=lst[i]+ans
                    break
                else:
                    num_list=num_list+[i]
                    if i%2:
                        i=i*3+1
                        ans+=1
                    else:
                        i/=2
                        ans+=1
            for ind,num in enumerate(num_list):
                lst[num]=ans-ind
            num_list=[]
        power_list=[(i,lst[i]) for i in range(lo,hi+1)]
        power_list.sort(key=lambda x:x[1])

        return power_list[k-1][0]
    

