class Solution:
    # O(n²)
    # def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    #     m , n = len(nums1),len(nums2)
    #     def fillUpper(m,nums):
    #         mapp1 = defaultdict(int)
    #         for i in range(m-1):
    #             for j in range(i+1,m):
    #                 mapp1[nums[i]*nums[j]]+=1
    #         return  mapp1
    #     mat1 = fillUpper(m,nums1)
    #     mat2 = fillUpper(n,nums2)
    #     res = 0
    #     for i in nums1:
    #         c=i**2 
    #         if(c in mat2):
    #             res+=mat2[c]
    #     for i in nums2:
    #         c= i**2 
    #         if(c in mat1):
    #             res+=mat1[c]       
    #     return res
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(nums1,nums2):
            res = 0
            for i in nums1:
                map1 = defaultdict(int)
                sq = i**2
                for j in nums2:
                    comp = sq/j
                    if(j in map1):
                        res+=map1[j]
                    map1[comp]+=1
            return res
        return count(nums1,nums2)+count(nums2,nums1)

