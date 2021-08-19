class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(a, b):
            ans = 0
            hashm = {}
            for i in a:
                if i * i not in hashm:
                    hashm[i * i] = 1
                else:
                    hashm[i * i] = hashm[i * i] + 1
            for i in range(len(b)):
                for j in range(i + 1, len(b)):
                    if b[i] * b[j] in hashm:
                        ans = ans + hashm[b[i] * b[j]]
            return ans
        return helper(nums1, nums2) + helper(nums2, nums1)
