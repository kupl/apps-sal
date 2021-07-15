class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        comp1, comp2 = defaultdict(set), defaultdict(set)
        
        if not nums1 or not nums2: return 0
        n, m = len(nums1), len(nums2)
        ans = 0
        
        c1, c2 = Counter([num**2 for num in nums1]), Counter([num**2 for num in nums2])
        
        for i in range(n):
            for j in range(i+1, n):
                prod = nums1[i]*nums1[j]
                ans += c2[prod]
                
        for i in range(m):
            for j in range(i+1, m):
                prod = nums2[i]*nums2[j]
                ans += c1[prod]
                
        return ans
