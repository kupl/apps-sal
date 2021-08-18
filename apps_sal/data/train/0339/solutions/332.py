class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        memo1 = collections.defaultdict(set)
        memo2 = collections.defaultdict(set)
        for i in range(len(nums1)):
            memo1[nums1[i]].add(i)
        for i in range(len(nums2)):
            memo2[nums2[i]].add(i)

        cnt = 0
        for i in range(len(nums1)):
            sq = nums1[i] * nums1[i]
            for j in range(len(nums2)):
                if nums2[j] > sq:
                    break
                if sq % nums2[j] != 0:
                    continue
                target = sq // nums2[j]
                if target in memo2:
                    cnt += len(memo2[target])
                    if j in memo2[target]:
                        cnt -= 1
        for i in range(len(nums2)):
            sq = nums2[i] * nums2[i]
            for j in range(len(nums1)):
                if nums1[j] > sq:
                    break
                if sq % nums1[j] != 0:
                    continue
                target = sq // nums1[j]
                if target in memo1:
                    cnt += len(memo1[target])
                    if j in memo1[target]:
                        cnt -= 1
        return cnt // 2
