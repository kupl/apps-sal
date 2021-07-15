class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=-1
        l=nums
        while 1:
            tf=0
            for i in range(len(nums)):
                if l[i]>0:
                    tf=1
                    if l[i]%2:
                        l[i]-=1
                        ans+=1
                    if l[i]:
                        l[i]//=2
            if not tf:
                break
            ans+=1
        return ans
