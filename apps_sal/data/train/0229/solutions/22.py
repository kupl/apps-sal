class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        # Eliminate zero
        negative = []
        positive = []

        zero_numbers = 0
        for a in A:
            if a < 0:
                negative.append(abs(a))
            elif a > 0:
                positive.append(a)
            else:
                zero_numbers += 1

        if zero_numbers % 2:
            return False

        negative.sort()
        positive.sort()
        # print(negative, positive)

        return self.helper(negative) and self.helper(positive)

    def helper(self, nums):
        while nums:
            cur_num = nums[0]
            idx = self.binarySearch(nums, 2 * cur_num)
            # print('helper',nums[0], idx)
            if idx == -1:
                return False
            nums.pop(idx)
            nums.pop(0)
            if len(nums) == 1:
                return False

        return True

    def binarySearch(self, nums, key):

        head = 0
        tail = len(nums) - 1
        # print(nums, key)

        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] > key:
                tail = mid - 1
            elif nums[mid] < key:
                head = mid + 1
            else:
                return mid

        return -1
