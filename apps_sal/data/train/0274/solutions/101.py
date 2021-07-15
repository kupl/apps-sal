class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)==1:
            return 1
        
        #nums.sort()
        #nums = [8,2,4,7]
        
        maxL=0
        beg=0
        #end=1
        '''
        while beg<len(nums)-1:
            #mx=max(nums[beg:(end+1)])
            #mn=min(nums[beg:(end+1)])
            while end<len(nums) and max(nums[beg:(end+1)])-min(nums[beg:(end+1)])<=limit:
                maxL=max(maxL, end-beg+1)
                end+=1
            beg+=1
            end=beg+1
        return maxL
        '''
        minQueue, maxQueue = collections.deque([]), collections.deque([])
        #minQueue, maxQueue=[], []
        #minQueue increasing, maxQueue decreasing
        
        #minQueue.append(nums[beg])
        #maxQueue.append(nums[beg])
        end=beg  
        while end<len(nums):
            
            #need while loop because if minQueue=[3,4,7], nums[end]=2
            #then since minQueue must be increasing and need to append nums[end]=2
            #so must remove 3,4, and 7
            while len(minQueue)>0 and nums[end]<minQueue[-1]:
                minQueue.pop()
            minQueue.append(nums[end]) #[2]
            
            #print(\" min: \", minQueue)
            
            while len(maxQueue)>0 and nums[end]>maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(nums[end]) #[7,2]
            
            
            if maxQueue[0]-minQueue[0]<=limit:
                maxL=max(maxL, end-beg+1)
            else:
                if maxQueue[0]==nums[beg]:
                    maxQueue.popleft()  #[1]
                    #maxQueue.pop(0)  #[1]
                if minQueue[0]==nums[beg]:
                    minQueue.popleft()  #[1]
                    #minQueue.pop(0)  #[1]
                beg+=1
            end+=1
            
        return maxL
