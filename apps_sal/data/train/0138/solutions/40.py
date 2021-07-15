class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def solve(arr):
            maxy = 0
            count = 0
            for i in j:
                if i < 0:
                    count += 1
            if count % 2 == 0:
                maxy = max(maxy,len(j))
            else:
                for i in range(len(j)):
                    if j[i] < 0:
                        m1 = i 
                        m2 = len(j) - m1 -1 
                        m3 = max(m1,m2)
                        maxy = max(maxy,m3)
                        break
                for i in range(len(j)-1,-1,-1):
                    if j[i] < 0:
                        m1 = i 
                        m2 = len(j) - m1 - 1 
                        m3 = max(m1,m2)
                        maxy = max(maxy,m3)
                        break
            return maxy
        res = []
        maxy = 0
        flag = 1
        i = 0
        for j in range(i,len(nums)):
            if nums[j] == 0:
                res.append(nums[i:j])
                i = j+1
                flag = 0
        if flag == 1:
            res.append(nums)
        elif flag == 0:
            res.append(nums[i:])
        nums = res
        for j in nums:
            maxy = max(maxy,solve(j))
        return maxy

