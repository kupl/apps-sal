class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def count(nums1, nums2):
            pairs = []
            N1, N2 = len(nums1), len(nums2)
            result = 0

            for i in range(N2):
                for j in range(i + 1, N2):
                    pairs.append((nums2[i], nums2[j]))
            
            Ns = collections.Counter(nums1)
            for u, v in pairs:
                if (u * v) ** 0.5 in Ns:
                    result += Ns[(u * v) ** 0.5]

            return result
        
        return count(nums1, nums2) + count(nums2, nums1)
