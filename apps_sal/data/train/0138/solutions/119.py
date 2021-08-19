class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ll = len(nums)
        if ll == 0:
            return 0

        curmax = 0
        submax = 0
        q = [0]
        nums.append(0)
        for ii in range(ll + 1):
            if nums[ii] == 0:
                curmax = ii - q[0]
                # print(submax,curmax,q)
                if len(q) % 2 == 0:
                    curmax = max(ii - q[1] - 1, q[-1] - q[0])
                submax = max(submax, curmax)
                q = [ii + 1]
                curmax = 0
            elif nums[ii] < 0:
                q.append(ii)

            submax = max(submax, curmax)
        return submax
