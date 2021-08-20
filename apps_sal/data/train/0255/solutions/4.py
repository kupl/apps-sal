class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        if len(nums)<=1:
            return 0
        dist=1
        explored ={}
        Q =[]
        explored[0]=dist
        Q.append(0)
        levelup = 0
        while Q[-1]+1 < len(nums):
            print(Q)
            v = Q[0]
            Q.pop(0)
            before=len(explored)
            for i in range(nums[v]):
                if not (v+i+1) in explored:
                    explored[v+i+1] = dist
                    Q.append(v+i+1)
            if v== levelup:
                dist+=1
                levelup=Q[-1]
            print(Q)
        return explored[len(nums)-1]
        """
        cur = 0
        ans = 0
        maxstep = 0
        for i in range(0, len(nums) - 1):
            maxstep = max(maxstep, i + nums[i])
            if i == cur:
                ans += 1
                cur = maxstep
        return ans
