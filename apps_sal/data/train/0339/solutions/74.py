class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # (i, j, k) if nums1[i]2 == nums2[j] * nums2[k]
        # (i, j, k) if nums2[i]2 == nums1[j] * nums1[k]

        n = len(nums1)
        m = len(nums2)
        n2dict = defaultdict(int)
        m2dict = defaultdict(int)
        for x in nums1:
            n2dict[x * x] += 1
        for x in nums2:
            m2dict[x * x] += 1
        # n2 = [x*x for i,x in enumerate(nums1)]
        # n2c= Counter(n2)
        # m2 = [x*x for i,x in enumerate(nums2)]
        # m2c= Counter(m2)
        out = 0

       #print(n2, m2)
        #print(n2c, m2c)

        for i in range(m):
            for j in range(i + 1, m):
                key = nums2[i] * nums2[j]
                # print(key)
                if nums2[i] * nums2[j] in n2dict:
                    out += (n2dict[key])
                    #print(key, nums2[i], nums2[j])

        # print()
        for i in range(n):
            for j in range(i + 1, n):
                key = nums1[i] * nums1[j]

                # print(key)
                if key in m2dict:
                    out += (m2dict[key])
                    #print(key, nums1[i], nums1[j])

        return out
