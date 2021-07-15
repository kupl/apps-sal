class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for i in range(len(nums1)):
            dic = collections.defaultdict(int)
            for j in range(len(nums2)):
                target = (nums1[i] **2) / nums2[j]
                if target in dic:
                    result += dic[target]
                dic[nums2[j]] += 1
                
        for i in range(len(nums2)):
            dic = collections.defaultdict(int)
            for j in range(len(nums1)):
                target = nums2[i] **2 / nums1[j]
                if target in dic:
                    result += dic[target]
                dic[nums1[j]] += 1
        return result
