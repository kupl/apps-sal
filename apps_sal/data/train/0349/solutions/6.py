class Solution:

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        count = collections.Counter(nums)
        take = [0] * (1 + nums[-1])
        delete = [0] * (1 + nums[-1])
        try:
            take[1] = count[1]
        except KeyError:
            take[1] = 0
        for i in range(2, nums[-1] + 1):
            print(i)
            try:
                delete[i] = max(take[i - 1], delete[i - 1])
                take[i] = i * count[i] + max(take[i - 2], delete[i - 1])
            except KeyError:
                continue
        print(take)
        print(delete)
        res = max(take[-1], delete[-1])
        return res
