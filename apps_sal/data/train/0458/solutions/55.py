class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        '''
        property of modulo
        (a+b)%p=(a%p+b%p)%p
        
        s=sum(nums)
        we want to find [s-(sumJ-sumI)]%p==0
        s-(sumJ-sumI)=np
        s-np=sumJ-sumI
        sumI=sumJ-s+np
        
        sumI%p=(sumJ-s+np)%p=(sumJ%p-s%p+np%p)%p=(sumJ%p-s%p)%p=(sumJ%p-k)%p
        
        
        '''
        n=len(nums)
        k=sum(nums)%p
        if not k:
            return 0
        
        d=defaultdict(int)
        d[0]=-1
        sumJ=0
        res=float('inf')
        for i,num in enumerate(nums):
            sumJ+=num
            sumJ_mod_p=sumJ%p
            sumI_mod_p=(sumJ_mod_p-k)%p
            if sumI_mod_p in d:
                res=min(res,i-d[sumI_mod_p])
            d[sumJ_mod_p]=i
        return res if res!=n else -1
