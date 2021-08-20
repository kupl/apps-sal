class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def cal(arr1, arr2):
            tmp = 0
            for n1 in arr1:
                n1pow2 = n1 * n1
                h = collections.defaultdict(int)
                for (idx, n2) in enumerate(arr2):
                    if n1pow2 / n2 in h:
                        tmp += h[n1pow2 // n2]
                    h[n2] += 1
            return tmp
        return cal(nums1, nums2) + cal(nums2, nums1)
