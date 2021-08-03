class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <= 0:
            return -1
        pivot = self.find_pivot(0, length - 1, nums)
        print(pivot)
        search_index_A = self.binary_search(0, max(pivot - 1, 0), nums, target)
        search_index_B = self.binary_search(pivot, length - 1, nums, target)
        if search_index_A >= 0:
            return search_index_A
        elif search_index_B >= 0:
            return search_index_B
        else:
            return -1

    def find_pivot(self, left_ind, right_ind, nums):
        mid = left_ind + (right_ind - left_ind) // 2
        if left_ind == right_ind:
            return left_ind
        elif nums[mid] < nums[mid - 1]:
            return mid
        elif nums[right_ind] < nums[mid]:
            return self.find_pivot(mid + 1, right_ind, nums)
        else:
            return self.find_pivot(left_ind, max(0, mid - 1), nums)

    def binary_search(self, left_ind, right_ind, nums, target):
        mid = left_ind + (right_ind - left_ind) // 2
        print(nums)
        print(mid)
        if nums[mid] == target:
            return mid
        elif left_ind == right_ind:
            return -1
        elif nums[mid] < target:
            return self.binary_search(mid + 1, right_ind, nums, target)
        else:
            return self.binary_search(left_ind, max(left_ind, mid - 1), nums, target)

# [5,1,3]
# [0]

# find_pivot(0,2,[5,1,3])
# left = 0
# right = 2
# mid = 0 + 2//2 = 1
# nums[mid] < nums[mid-1]
# pivot = 1
# binary_search(0, max(pivot-1,0), ...)
# left = 0, right = 0
# search_index_A = -1
# binary_search(pivot, length-1, ...)
# left = 1, right = 2
# mid = 1 + (2-1)//2 = 1
# binary_search(1, max(0,0), ...)
# search_index_B = -1
