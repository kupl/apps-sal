class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        if len(croakOfFrogs) % 5 != 0:
            return -1
        nums = [0] * 5
        
        dic = {'c': 0, 'r': 1, 'o':2, 'a': 3, 'k' : 4}
        res = 1
        for ch in croakOfFrogs:
            if dic[ch] != 0 and nums[dic[ch]] >= nums[dic[ch] - 1]:
                return -1
            
            nums[dic[ch]] += 1
            res = max(res, nums[0])
            if ch == 'k':
                for i in range(5):
                    nums[i] -= 1        
        
            
        return res
