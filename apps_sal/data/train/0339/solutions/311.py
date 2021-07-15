class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def getRes(arr1, arr2):
            count = 0
            n = len(arr2)
            max2 = arr2[-1]
            for i in range(len(arr1)):
                if arr1[i] > max2: break
                target = arr1[i] ** 2
                
                seen = collections.defaultdict(int)
                for j in range(n):
                    if target / arr2[j] in seen:
                        count += seen[target / arr2[j]]
                    seen[arr2[j]] += 1
                        
            
            return count
        nums1.sort()
        nums2.sort()
        return getRes(nums1, nums2) + getRes(nums2, nums1)
