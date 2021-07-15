class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m1_square,m2_square={},{}
        for x in nums1:
            x_square = x**2
            m1_square[x_square]=m1_square.get(x_square,0)+1
            
        for x in nums2:
            x_square=x**2
            m2_square[x_square]=m2_square.get(x_square,0)+1
        
        m,n=len(nums1),len(nums2)
        ans = 0
        for j in range(m-1):
            for k in range(j+1,m):
                if (nums1[j]*nums1[k]) in m2_square:
                    ans+=m2_square[nums1[j]*nums1[k]]
        for j in range(n-1):
            for k in range(j+1, n):
                if (nums2[j]*nums2[k]) in m1_square:
                    ans+=m1_square[nums2[j]*nums2[k]]
        return ans
