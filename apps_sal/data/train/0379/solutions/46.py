class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        i1 = len(nums1) - 1
        i2 = len(nums2) - 1
        paths = []
        while i1 >= 0 and i2 >= 0:
          if nums1[i1] > nums2[i2]:
            sum1 += nums1[i1]
            i1 -= 1
          elif nums1[i1] < nums2[i2]:
            sum2 += nums2[i2]
            i2 -= 1
          else:
            paths.append((sum1 + nums1[i1], sum2 + nums1[i1]))
            sum1 = sum2 = 0
            i1 -= 1
            i2 -= 1
        if i1 >= 0:
          paths.append((sum1 + sum(nums1[:i1+1]), sum2))
        if i2 >= 0:
          paths.append((sum1, sum2 + sum(nums2[:i2+1])))
        
        ans = 0
        for l, r in paths:
          ans += max(l, r)
          ans %= 10**9 + 7
        return ans      
            

        
        # print(nums1)
        # print(nums2)
        # print('')
        def _dp(ii, its1, val):
          # print(ii, its1, val)
          nums = nums1 if its1 else nums2
          oums = nums2 if its1 else nums1
          if ii == len(nums):
            return val
          # path.append((its1, nums[ii]))
          if nums[ii] in oums:
            ix = oums.index(nums[ii])
            # path.append((not its1, nums[ii]))
            opt = _dp(ix + 1, not its1, val + nums[ii])
          else:
            opt = 0
          cur = _dp(ii + 1,     its1, val + nums[ii]) 
          return max([opt, cur])
            
        
        return max([_dp(0, True, 0), _dp(0, False, 0)])
      

