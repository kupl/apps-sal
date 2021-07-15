class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
        
        dp1:[30,28,23,18,10, 0]
        dp2: [28,24,18,9, 0]
        
        dp1[i] = if nums1[i]==nums2[j]: max(nums1[i]+dp1[i+1], nums1[i]+dp2[j+1])
                    else: nums1[i]+dp1[i+1]
        (dp1[len(nums1)]=0)
        dp2[i] = if nums1[j]==nums2[i]: max(nums1[i]+dp1[j+1], nums1[i]+dp2[i+1])
        
        i1, i2 = len(nums1)-1, len(nums2)-1
        while i1>=0 and i2>=0:
            if nums1[i1] == nums[i2]:
                dp1[i1] = max(nums1[i1]+dp1[i1+1], nums1[i2]+dp2[i2+1])
                i1-=1
                i2-=1
            elif nums1[i1] > nums[i2]:
                dp1[i1] = nums1[i1]+dp1[i1+1]
                i1-=1
            else:
                dp2[i2] = nums2[i2]+dp2[i2+1]
                i2-=1
        if i1>=0:
            return max(sum()+dp1[i1+1], dp2[i2+1])
            
        '''
        dp1 = [0 for _ in range(len(nums1)+1)]
        dp2 = [0 for _ in range(len(nums2)+1)]
        i1, i2 = len(nums1)-1, len(nums2)-1
        while i1>=0 and i2>=0:
            if nums1[i1] == nums2[i2]:
                dp1[i1] = max(nums1[i1]+dp1[i1+1], nums2[i2]+dp2[i2+1])
                dp2[i2] = max(nums1[i1]+dp1[i1+1], nums2[i2]+dp2[i2+1])
                i1-=1
                i2-=1
            elif nums1[i1] > nums2[i2]:
                dp1[i1] = nums1[i1]+dp1[i1+1]
                i1-=1
            else:
                dp2[i2] = nums2[i2]+dp2[i2+1]
                i2-=1
        # print(dp1)
        # print(dp2)
        if i1>=0:
            return max(sum(nums1[:i1+1])+dp1[i1+1], dp2[i2+1])%(10**9+7)
        else:
            return max(sum(nums2[:i2+1])+dp2[i2+1], dp1[i1+1])%(10**9+7)

