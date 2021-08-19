class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # similar to find cycle in the linked list
        # actually, here we have more than 1 logical linked list(with or without cycle)
        # begin with nums[0] can help us determining at least one cycled linked list of them
        fast, slow = nums[0], nums[0]
        while(True):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        ptr1 = nums[0]
        ptr2 = fast
        while(ptr1 != ptr2):
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
