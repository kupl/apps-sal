from collections import Counter


class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        return self.count_triplets(count1, count2) + self.count_triplets(count2, count1)

    def count_triplets(self, count1, count2):
        triplets = 0
        for (n1, c1) in count1.items():
            for (n2, c2) in count2.items():
                n3 = n1 ** 2 / n2
                c3 = count2[n3]
                if n2 == n3:
                    triplets += c1 * c3 * (c3 - 1) / 2
                else:
                    triplets += c1 * c2 * c3 / 2
        return int(triplets)
