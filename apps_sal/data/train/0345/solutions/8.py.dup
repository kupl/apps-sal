class Solution:

    def soln_exists(self, nums, m, i):
        index = 0
        for x in range(m):
            total = 0
            while True:
                total += nums[index]
                index += 1
                if (total > i):
                    break
                if index == len(nums):
                    return True
            index -= 1
        return False

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        work = 1
        while not self.soln_exists(nums, m, work):
            work *= 2
        not_work = work / 2
        while not_work < work - 1:
            middle = not_work / 2 + work / 2
            if self.soln_exists(nums, m, middle):
                work = middle
            else:
                not_work = middle
        return int(work)
