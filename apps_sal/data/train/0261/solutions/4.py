class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(nums, ind, i, j):

            big, scan = i, i

            nums[ind], nums[j] = nums[j], nums[ind]

            while scan < j:
                if nums[scan] > nums[j]:
                    nums[big], nums[scan] = nums[scan], nums[big]
                    big += 1

                scan += 1

            nums[j], nums[big] = nums[big], nums[j]
            return big

        i, j = 0, len(nums) - 1
        while i <= j:
            ind = random.randint(i, j)
            new_ind = partition(nums, ind, i, j)
            if new_ind == k - 1:
                return nums[new_ind]
            elif new_ind < k - 1:
                i = new_ind + 1
            else:
                j = new_ind - 1

        return -1
