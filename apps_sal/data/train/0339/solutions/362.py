class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1 = Counter([n**2 for n in nums1])
        sq2 = Counter([n**2 for n in nums2])
        triplets = self.count_triplets(sq1, nums2)
        triplets += self.count_triplets(sq2, nums1)
        return triplets

    def count_triplets(self, sqs: List[int], nums: List[int]) -> int:
        pairs = defaultdict(int)
        triplets = 0
        for n in nums:
            if n in pairs:
                triplets += pairs[n]
            for k in sqs:
                pairs[k / n] += sqs[k]
        return triplets
