class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        # nums1.sort()
        # nums2.sort()
        for i in range(len(nums1)):
            hashmap = collections.defaultdict(int)
            for j in range(len(nums2)):
                if nums1[i] * nums1[i] / nums2[j] in hashmap:
                    ans += hashmap[nums1[i] * nums1[i] / nums2[j]]
                    # print(i,j, hashmap)
                hashmap[nums2[j]] += 1
                
        for i in range(len(nums2)):
            hashmap = collections.defaultdict(int)
            for j in range(len(nums1)):
                if nums2[i] * nums2[i] / nums1[j] in hashmap:
                    ans += hashmap[nums2[i] * nums2[i] / nums1[j]]
                    # print(i,j, hashmap)
                hashmap[nums1[j]] += 1
            
            # for j in range(len(nums2) - 1):
            #     k = j + 1
            #     while k < len(nums2):
            #         if nums1[i] * nums1[i] == nums2[j] * nums2[k]:
            #             ans += 1
            #             # print((i,j,k))
        #     #         k += 1
        # for i in range(len(nums2)):
        #     j, k = 0, len(nums1) - 1
        #     while j < k:
        #         if nums2[i] * nums2[i] == nums1[j] * nums1[k]:
        #             ans += 1
        #             j += 1
        #         elif nums2[i] * nums2[i] < nums1[j] * nums1[k]:
        #             k -= 1
        #         else:
        #             j += 1
        return ans

