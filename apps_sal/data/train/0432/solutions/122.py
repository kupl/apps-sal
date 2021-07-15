class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        c=Counter(nums)
        keys=sorted(c)
        for key in keys:
            while c[key]>0:
                for i in range(k):
                    if key+i in list(c.keys()) and c[key+i]>0:
                        c[key+i]-=1
                    else:
                        return False
        return True

                
                    

