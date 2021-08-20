import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        return self.binSearch(1, nums[-1], nums, threshold)

    def binSearch(self, head, tail, nums, threshold):
        if head == tail:
            return head
        mid = (tail - head) // 2 + head
        ct = 0
        flag = True
        for num in nums:
            ct += math.ceil(num / mid)
            if ct > threshold:
                flag = False
                break
        if not flag:
            return self.binSearch(mid + 1, tail, nums, threshold)
        else:
            return self.binSearch(head, mid, nums, threshold)
