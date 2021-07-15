class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def check(l1, l2):
            res = {}
            j = 0
            while j < len(l2):
                k = j+1
                while k < len(l2):
                    res[l2[j] * l2[k]] = res.get(l2[j] * l2[k], 0) + 1
                    k += 1
                j += 1
            
            
            ans = 0
            while l1:
                node = l1.pop()
                if node in res:
                    ans += res[node]
            return ans

            
        squares1 = [x*x for x in nums1]
        squares2 = [x*x for x in nums2]
        return check(squares1, nums2) + check(squares2, nums1)
