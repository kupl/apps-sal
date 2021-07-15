class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1.sort()
        # nums2.sort()
        
        
        def count(A, B):
            res = 0
            n1 = len(A)
            n2 = len(B)
            for i in range(n1):
                target = A[i]**2
                d = collections.defaultdict(int)
                for num in B:
                    if target/num in d:
                        res += d[target/num]
                    d[num] += 1
            return res
                        
            
            
            
        return count(nums1, nums2) + count(nums2, nums1)
