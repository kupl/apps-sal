class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        

        def multi(arr):
            D = {}
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[i] * arr[j] not in D:
                        D[arr[i] * arr[j]] = 1
                    else:
                        D[arr[i] * arr[j]] += 1
            return D
                    
        nums1_multi = multi(nums1)
        nums2_multi = multi(nums2)
        res = 0
        
        for i in nums1:
            res += nums2_multi.get(i**2,0)
            
        for i in nums2:
            res += nums1_multi.get(i**2,0)

        
        return res     


