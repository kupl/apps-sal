class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            s = [n * n for n in nums1]
            count = 0
            d = collections.defaultdict(list)
            for i in range(len(nums2)):
                d[nums2[i]].append(i)

            for n in s:
                for i in range(len(nums2)):
                    if n % nums2[i] == 0 and n // nums2[i] in d:
                        if nums2[i] == n // nums2[i]:
                            count += len(d[n // nums2[i]]) - 1
                        else:
                            count += len(d[n // nums2[i]])
            return count // 2
        return helper(nums1, nums2) + helper(nums2, nums1)
