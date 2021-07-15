class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #Full of one's or Zero
        zc,oc=0,0
        for i,v in enumerate(nums):
            if v:oc+=1
            else:zc+=1
        if oc==len(nums):return oc-1
        elif zc==len(nums):return 0
        elif zc==1: return oc
        elif oc==1: return 1
        else:
            #calculate left one's once to make your algo look better
            l=r=0
            for i,v in enumerate(nums):
                if v==1:
                    l+=1
                else:
                    break
            st=i+1
            #print(i,nums[i])
            po=i
            maxo,maxi=-1,-1
            while(st < len(nums)):
                if nums[st]==1:
                    r+=1
                    st+=1
                    continue
                else:
                    v=l+r
                    if maxo < v:
                        maxo=v
                        maxi=po
                    po=st
                    l=r
                    r=0
                    st+=1
            maxo=max(maxo,l+r)
            return maxo
                    
                    
                
                    

