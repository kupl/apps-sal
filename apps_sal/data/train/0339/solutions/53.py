class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def findTriplet2(arr1, arr2):
            result = 0
            m = len(arr2)
            count = collections.Counter([x**2 for x in arr1])
            for j in range(m):
                for k in range(j + 1, m):
                    if arr2[j] * arr2[k] in list(count.keys()):
                        result += count[arr2[j] * arr2[k]]
            return result

        def findTriplet(arr1, arr2):
            n, m = len(arr1), len(arr2)
            triplets = 0
            for i in range(n):
                for j in range(m):
                    for k in range(j + 1, m):
                        if arr1[i]**2 == arr2[j] * arr2[k]:
                            triplets += 1
            return triplets
        return findTriplet2(nums1, nums2) + findTriplet2(nums2, nums1)
