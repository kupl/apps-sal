from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.triples(nums1, nums2) + self.triples(nums2, nums1)

    def triples(self, nums1, nums2):
        res = 0
        for n1 in nums1:
            visited = defaultdict(int)
            for n2 in nums2:
                if n1 * n1 % n2 == 0:
                    res += visited[n1 * n1 // n2]

                visited[n2] += 1

        return res
