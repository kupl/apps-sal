class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        m = len(nums2)
        sq1 = list(map(lambda x:x**2,nums1))
        sq2 = list(map(lambda x:x**2,nums2))
        d1 = dict()
        d2 = dict()
        for num1 in list(set(nums1)):
            d1[num1] = dict()
            for i in range(n):
                if nums1[i] == num1:
                    if i == 0:
                        d1[num1][i] = 1
                    else:
                        d1[num1][i] = d1[num1][i-1]+1
                else:
                    if i == 0:
                        d1[num1][i] = 0
                    else:
                        d1[num1][i] = d1[num1][i-1]
        
        for num2 in list(set(nums2)):
            d2[num2] = dict()
            for i in range(m):
                if nums2[i] == num2:
                    if i == 0:
                        d2[num2][i] = 1
                    else:
                        d2[num2][i] = d2[num2][i-1]+1
                else:
                    if i == 0:
                        d2[num2][i] = 0
                    else:
                        d2[num2][i] = d2[num2][i-1]
        
        for i in range(n):
            for j in range(m-1):
                tmp = sq1[i]//nums2[j]
                if sq1[i]%nums2[j] == 0:
                    if tmp not in d2:
                        continue
                    ans += d2[tmp][m-1] - d2[tmp][j]
        
        for j in range(m):
            for i in range(n-1):
                tmp = sq2[j]//nums1[i]
                if sq2[j]%nums1[i] == 0:
                    if tmp not in d1:
                        continue
                    ans += d1[tmp][n-1] - d1[tmp][i]
        return ans
