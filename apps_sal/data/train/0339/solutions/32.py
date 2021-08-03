class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        dict1 = {}
        dict2 = {}
        for i in nums1:
            x = i * i
            if x not in dict1.keys():
                dict1[x] = 1
            else:
                dict1[x] = dict1[x] + 1
        for j in nums2:
            x = j * j
            if x not in dict2.keys():
                dict2[x] = 1
            else:
                dict2[x] = dict2[x] + 1
        print(dict1)
        print(dict2)
        for j in range(0, len(nums2)):
            for k in range(j + 1, len(nums2)):
                if nums2[k] * nums2[j] in dict1.keys():
                    count = count + dict1[nums2[j] * nums2[k]]
        for j in range(0, len(nums1)):
            for k in range(j + 1, len(nums1)):
                if nums1[j] * nums1[k] in dict2.keys():
                    count = count + dict2[nums1[j] * nums1[k]]
        return count
