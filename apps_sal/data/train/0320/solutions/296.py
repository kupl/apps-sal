class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        onesCount = 0
        aboveOneIdxs = []
        for idx, n in enumerate(nums):
            if n == 1:
                onesCount += 1
            elif n > 1:
                aboveOneIdxs.append(idx)
                
        while onesCount + len(aboveOneIdxs) != 0:
            count += onesCount
            onesCount = 0
            newAboveOneIdxs = []
            for idx in aboveOneIdxs:
                if nums[idx] % 2 != 0:
                    nums[idx] -= 1
                    count += 1
                nums[idx] //= 2
                if nums[idx] == 1:
                    onesCount += 1
                else:
                    newAboveOneIdxs.append(idx)
            if len(aboveOneIdxs) > 0:
                count += 1 # multiplied by 2
            aboveOneIdxs = newAboveOneIdxs
                    
        return count

