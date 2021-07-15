class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i,j=0,0
        nums.append(float('inf'))
        qmin=collections.deque() # monotonic non-decreasing
        qmax=collections.deque() # non-increasing 
        qmin.append(0)
        qmax.append(0)
        ans=0
        
        while j<len(nums)-1:
            while j<len(nums)-1 and nums[qmax[0]]-nums[qmin[0]]<=limit:
                ans = max(ans, j-i+1)
                j+=1
                
                while qmax and nums[qmax[-1]]<nums[j]:
                    qmax.pop()
                qmax.append(j)
                
                while qmin and nums[qmin[-1]]>nums[j]:
                    qmin.pop()
                qmin.append(j)
                
                
            # only one can happen
            while qmax and nums[qmax[0]] - nums[j] > limit:
                i = qmax.popleft()+1
                
            while qmin and nums[j] - nums[qmin[0]] > limit:
                i = qmin.popleft()+1
                
        return ans
