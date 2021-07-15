class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        
        
        i = 0 
        for a in nums:
            # print(a)
            # print(maxd)
            # print(mind)
            while len(maxd) and a>maxd[-1]:
                maxd.pop()
            while len(mind) and a<mind[-1]:
                mind.pop();
            # print(maxd)
            # print(mind)
            maxd.append(a)
            mind.append(a)
            # print(maxd)
            # print(mind)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                    
                i += 1
     
        return len(nums) - i
