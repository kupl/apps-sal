class Solution:
     def splitArray(self, nums, m):
         """
         :type nums: List[int]
         :type m: int
         :rtype: int
         """
         accum = [0]
         N = len(nums)
         mmm = max(nums)
         if m >= N:
             return mmm
         res = 0
         for i in nums:
             res += i
             accum.append(res)
         lower, upper = mmm , sum(nums)
         while lower < upper:
             mid = (lower + upper) // 2
             if not self.isSplitable(accum, m, mid):
                 lower = mid + 1
             else:
                 upper = mid
         # print(lower, upper)
         return upper
     def isSplitable(self, accum, m, maxx):
         start = 0
         N = len(accum)
         end = 0
         count = 0
         while end < N and count < m:
             if accum[end] - accum[start] > maxx:
                 # print('start: ', start, 'end:', end, 'sum', accum[end - 1] - accum[start])
                 start = end - 1
                 count += 1
             end += 1
             #print (count, end)
         if accum[-1] - accum[start] > maxx: #收尾
             count += 2
         else:
             count += 1
         # print('start: ', start, 'end:', end, 'sum', accum[end - 1] - accum[start])
         # print (end, count)
         if end != N or count > m:
             return False
         return True
