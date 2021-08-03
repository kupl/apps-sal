class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        fn = -1
        zi = -1
        cn = 0
        dig = 0
        maxdig = 0
        for i in range(len(nums)):
            if(nums[i] < 0):
                cn += 1
                if(fn == -1):
                    fn = i
            if(nums[i] == 0):
                fn = -1
                cn = 0
                zi = i
            else:
                if(cn % 2 == 0):
                    maxdig = max(i - zi, maxdig)
                else:
                    maxdig = max(i - fn, maxdig)
        return maxdig
