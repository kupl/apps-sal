class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''Input: nums1 = [7,4], nums2 = [5,2,8,9]
        Output: 1
        Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
        '''
        if not nums1 or not nums2:
            return 0

        res = 0
        newlist1 = collections.defaultdict(set)
        newlist2 = collections.defaultdict(set)

        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                key = nums2[i] * nums2[j]
                newlist1[key].add((i, j))

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                key = nums1[i] * nums1[j]
                newlist2[key].add((i, j))
        # print(newlist)

        for n in nums1:
            if n**2 in newlist1:
                res += len(newlist1[n**2])
        for n in nums2:
            if n**2 in newlist2:
                res += len(newlist2[n**2])
        return res
