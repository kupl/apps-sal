from collections import Counter
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        res = 1        
        count = defaultdict(int)
        inverseCount = defaultdict(set)
        for i in range(len(nums)):
            if count[nums[i]] in inverseCount:
                inverseCount[count[nums[i]]].remove(nums[i])
                if len(inverseCount[count[nums[i]]]) == 0:
                    inverseCount.pop(count[nums[i]])
            count[nums[i]] += 1
            inverseCount[count[nums[i]]].add(nums[i])

            if self.canBeEqualFreq(inverseCount):
                res = i+1
        
        return res
            
            
    def canBeEqualFreq(self, ic):
        ickeys, icvalues = list(ic.keys()), list(ic.values())
        if len(ic) == 1:
            return len(icvalues[0])==1 or 1 in list(ic.keys())
        
        if len(ic) > 2:
            return False
        # case 1: 1,2,2,2,3,3,3
        if 1 in ickeys and len(ic[1])==1:
            return True
        # case 2: 1,1,2,3
        if (ickeys[0] - ickeys[1] == 1 and len(ic[ickeys[0]])==1) or (ickeys[1] - ickeys[0] == 1 and len(ic[ickeys[1]])==1) :
            return True
        
        return False

