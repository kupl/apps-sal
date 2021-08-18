class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def countTriplets(nums1, nums2):
            num2idx = defaultdict(list)
            for i, n in enumerate(nums2):
                num2idx[n].append(i)

            res = 0
            ct1 = Counter(nums1)
            for n in ct1:
                nsq = n**2
                for i, n1 in enumerate(nums2):
                    n2, mod2 = divmod(nsq, n1)
                    if mod2 == 0 and n2 in num2idx:
                        res += len([x for x in num2idx[n2] if x > i]) * ct1[n]
            return res

        return countTriplets(nums1, nums2) + countTriplets(nums2, nums1)
