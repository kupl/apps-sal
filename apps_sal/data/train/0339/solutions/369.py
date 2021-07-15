class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(arr1, arr2):
            res = 0
            dic = collections.Counter(arr1)
            for a in dic:
                counter = collections.Counter()
                for b in arr2:
                    c = a * a / b
                    if c in counter:
                        res += counter[c] * dic[a]
                    counter[b] += 1
            return res
        res = count(nums1, nums2)
        res += count(nums2, nums1)
        return res
