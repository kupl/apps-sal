class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = list(Counter(nums1).items())
        nums2 = list(Counter(nums2).items())

        def find(target, count1, arr):
            seen = Counter()
            ans = 0
            for a, count2 in arr:
                if target % a == 0:
                    if (b := target // a) != a:
                        ans += count1 * count2 * seen[b]
                    else:
                        ans += count1 * math.comb(count2, 2)
                seen[a] += count2
            return ans

        @lru_cache(None)
        def twoProduct1(target, count):
            return find(target, count, nums1)

        @lru_cache(None)
        def twoProduct2(target, count):
            return find(target, count, nums2)

        return sum(twoProduct2(a * a, c) for a, c in nums1) + sum(twoProduct1(a * a, c) for a, c in nums2)
