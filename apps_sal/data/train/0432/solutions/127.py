class Solution:
  def isPossibleDivide(self, nums, k):
    ctr = Counter(nums)
    for num in nums:
        start = num
        while ctr[start - 1]:
            start -= 1
        while start <= num:
            times = ctr[start]
            if times:
                for victim in range(start, start + k):
                    if ctr[victim] < times:
                        return False
                    ctr[victim] -= times
            start += 1
    return True
