class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2 == 0:
            target = sum_ / 2

            def myFun(t, nu):
                nu.sort()
                nu.reverse()
                for (index, item) in enumerate(nu):
                    if item == t:
                        return True
                    elif item > t:
                        return False
                    else:
                        nun = nu.copy()
                        del nun[index]
                        if myFun(t - item, nun):
                            return True
                        elif index == len(nu) - 1:
                            return False
            return myFun(target, nums)
        return False
