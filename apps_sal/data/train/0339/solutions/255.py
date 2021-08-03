class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        D = {}
        G = {}
        H = {}
        N1 = {}
        N2 = {}

        for i in range(len(nums1)):
            N1[nums1[i]] = 1
            for j in range(i + 1, len(nums1)):
                D[nums1[i] * nums1[j]] = 1

        for i in range(len(nums2)):
            N2[nums2[i]] = 1
            for j in range(i + 1, len(nums2)):
                G[nums2[i] * nums2[j]] = 1

        for i in range(len(nums1)):
            if nums1[i]**2 in G:
                if nums1[i]**2 not in H:
                    tmp = 0
                    for x in range(len(nums2)):
                        if nums1[i]**2 % nums2[x] == 0 and (nums1[i]**2) // nums2[x] in N2:
                            for y in range(x + 1, len(nums2)):
                                if nums2[x] * nums2[y] == nums1[i]**2:
                                    tmp += 1

                    H[nums1[i]**2] = tmp
                    ans += tmp

                else:
                    ans += H[nums1[i]**2]

        H = {}

        for i in range(len(nums2)):
            if nums2[i]**2 in D:
                if nums2[i]**2 not in H:
                    tmp = 0
                    for x in range(len(nums1)):
                        if nums2[i]**2 % nums1[x] == 0 and (nums2[i]**2) // nums1[x] in N1:
                            for y in range(x + 1, len(nums1)):
                                if nums1[x] * nums1[y] == nums2[i]**2:
                                    tmp += 1

                    H[nums2[i]**2] = tmp
                    ans += tmp

                else:
                    ans += H[nums2[i]**2]

        return ans
