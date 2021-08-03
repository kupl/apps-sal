class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def calc(a: List[int], b: List[int]):
            from collections import defaultdict
            freq = defaultdict(int)
            for ai in a:
                freq[ai] += 1
            _ans = 0
            for bi in b:
                t = bi * bi
                for k in freq:
                    if t % k != 0 or t / k not in freq:
                        continue
                    elif t / k == k:
                        _ans += freq[k] * (freq[k] - 1)
                    else:
                        _ans += freq[k] * freq[t / k]
            return int(_ans / 2)
        return calc(nums1, nums2) + calc(nums2, nums1)
