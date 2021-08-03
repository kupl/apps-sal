class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = set()
        for i in range(len(nums)):
            n = nums[i]
            if n not in st:
                st.add(n)
            else:
                return n
