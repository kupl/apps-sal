class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = self.sort(nums)
        if s.startswith("0"):
            return "0"
        else:
            return s

    def sort(self, nums):
        if not nums:
            return ""
        else:
            pivot = nums[0]
            left = []
            right = []
            for i in range(1, len(nums)):
                if self.compare(nums[i], pivot):
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            return self.sort(left) + str(pivot) + self.sort(right)

    def compare(self, num1, num2):
        num1, num2 = str(num1), str(num2)
        return int(num1 + num2) > int(num2 + num1)
