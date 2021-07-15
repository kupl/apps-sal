import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+100)
from collections import *

class Solution:
    def rec(self, t, i):
        if self.memo[t][i]!=-1:
            return self.memo[t][i]
    
        if i==0:
            return 0
        
        if t==0:
            res = self.rec(0, i-1)+self.nums1[i-1]
            
            if self.nums1[i-1] in self.idx2:
                res = max(res, self.rec(1, self.idx2[self.nums1[i-1]])+self.nums1[i-1])
        else:
            res = self.rec(1, i-1)+self.nums2[i-1]
            
            if self.nums2[i-1] in self.idx1:
                res = max(res, self.rec(0, self.idx1[self.nums2[i-1]])+self.nums2[i-1])
        
        self.memo[t][i] = res
        return res
    
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        self.idx1 = defaultdict(int)
        self.idx2 = defaultdict(int)
        
        for i in range(n):
            self.idx1[nums1[i]] = i
        
        for i in range(m):
            self.idx2[nums2[i]] = i
        
        self.memo = [[-1]*max(n+1, m+1) for _ in range(2)]
        return max(self.rec(0, n), self.rec(1, m))%(10**9+7)
