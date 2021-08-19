class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        # print(nums,k)
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for j in d:
            while d[j] > 0:
                for x in range(j, j + k):
                    if d.get(x, 0) > 0:
                        d[x] -= 1
                    else:
                        return False
        return True

        '''
        i=0
        while k<=len(nums):
            a=nums[0]
            for j in range(k):
                if a+j not in nums or len(nums)==0:
                    return False
                nums.remove(a+j)
            if len(nums)%k!=0:
                return False
            if len(nums)==0:
                return True
        return True
        
        while True :
            a=nums[0]
            for i in range(k):
                if a+i not in nums or len(nums)==0:
                    return False
                nums.remove(a+i)
            if len(nums)%k!=0:
                return False
            if len(nums)==0:
                return True
        '''
