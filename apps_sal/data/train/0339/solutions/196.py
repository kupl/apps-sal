class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        muti_set1 = set()
        muti_set2 = set()
        muti_dict1 = dict()
        muti_dict2 = dict()
        
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                v = nums1[i] * nums1[j]
                if v in muti_set1:
                    muti_dict1[str(v)] = muti_dict1[str(v)] + 1
                else:
                    muti_dict1[str(v)] = 1
                    muti_set1.add(v)
            
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                v = nums2[i] * nums2[j]
                if v in muti_set2:
                    muti_dict2[str(v)] = muti_dict2[str(v)] + 1
                else:
                    muti_dict2[str(v)] = 1
                    muti_set2.add(v)
        
        res = 0
        print(muti_set1)
        print(muti_set2)
        
        for _ in nums1:
            if _*_ in muti_set2:
                res = res + muti_dict2[str(_*_)]
        
        for _ in nums2:
            if _*_ in muti_set1:
                res = res + muti_dict1[str(_*_)]
        
        return res

