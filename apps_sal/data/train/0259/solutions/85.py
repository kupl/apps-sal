class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def dfs(m):
            r = 0
            for i in nums:
                r += math.ceil(i / m)
                if r > threshold:
                    return False
            return True
        l, r = 1, int(1e6)
        while l <= r:
            m = (l + r) // 2
            if dfs(m):
                r = m - 1
            else:
                l = m + 1
        return l
        '''
        for i in range(1,max(nums)):
            r=0
            n-=1
            for j in nums:
                if j%i==0:
                    r+=j//i
                else:
                    r+=(j//i)+1
            if r<=threshold:
                return i
        '''
