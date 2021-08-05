class Solution:
    def isPossibleDivide(self, nums, k):
        ctr = collections.Counter(nums)
        for num in nums:
            start = num
            while ctr[start - 1]:
                start -= 1
            while start <= num:
                while ctr[start]:
                    for victim in range(start, start + k):
                        if not ctr[victim]:
                            return False
                        ctr[victim] -= 1
                start += 1
        return True
