import bisect 
from collections import defaultdict
mod = 10**9+7
class Solution:
    d_nums1 = defaultdict(int)
    d_nums2 = defaultdict(int)
    dp = []
    def f(self, nums1, nums2, ar_ind, pos):
        if self.dp[ar_ind][pos]!=-1:
            return self.dp[ar_ind][pos]
        if ar_ind == 1:
            if pos == len(nums2):
                 self.dp[ar_ind][pos] = 0 
            elif self.d_nums1[nums2[pos]] == 0 and nums1[0]!=nums2[pos]:
                self.dp[ar_ind][pos] = (nums2[pos] + self.f(nums1,nums2,1,pos+1))
            else:
                self.dp[ar_ind][pos] = (nums2[pos] + max(self.f(nums1,nums2,1,pos+1),self.f(nums1,nums2,0,self.d_nums1[nums2[pos]]+1)))
        else:
            if pos == len(nums1):
                self.dp[ar_ind][pos] =  0
            elif self.d_nums2[nums1[pos]] == 0 and nums2[0]!=nums1[pos]:
                self.dp[ar_ind][pos] =  (nums1[pos] + self.f(nums1,nums2,0,pos+1))
            else:
                self.dp[ar_ind][pos] = (nums1[pos] + max(self.f(nums1,nums2,0,pos+1),self.f(nums1,nums2,1,self.d_nums2[nums1[pos]]+1)))
        return self.dp[ar_ind][pos]
                
    
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.d_nums1.clear()
        self.d_nums2.clear()
        for i in range(len(nums1)):
            self.d_nums1[nums1[i]] = i 
        for i in range(len(nums2)):
            self.d_nums2[nums2[i]] = i 
        self.dp = [[-1]*(len(nums1)+1)]
        self.dp.append([-1]*(len(nums2)+1))
        # print(self.dp)
        self.f(nums1,nums2,1,0)
        self.f(nums1,nums2,0,0)
        
        # print(self.dp)
        return max(self.dp[0][0],self.dp[1][0])%mod
