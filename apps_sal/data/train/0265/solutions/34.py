class Solution:
    
    def maxNonOverlapping(self, nums, target) -> int:
        hashMap = {0: -1} #totalSum -> inclusive ending index
        totalSum = 0
        answer = []
        count = 0
        for i in range(len(nums)):
            totalSum += nums[i]
            if totalSum - target in hashMap:
                answer.append([hashMap[totalSum-target] + 1, i])
            
            hashMap[totalSum] = i

        ending = None
        for i in answer:
            if ending is None or i[0] > ending:
                count += 1
                ending = i[1]
        return count 

