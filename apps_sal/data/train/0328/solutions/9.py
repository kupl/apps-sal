class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        minV = []
        for i in range(len(nums)):
            if i == 0:
                minV.append(nums[i])
            else:
                minV.append(min(nums[i], minV[-1]))
        st = []
        for j in range(len(nums) - 1, 0, -1):
            if not st or nums[j] <= st[-1]:
                st.append(nums[j])
            else:
                while st and nums[j] > st[-1]:
                    s3 = st.pop()
                if s3 > minV[j]:
                    return True
                st.append(nums[j])
        return False
