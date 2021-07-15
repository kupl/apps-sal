import sys
input = sys.stdin.readline
from collections import *

class Solution:
    def calc(self, l1, l2):
        cnt = Counter(l2)
        res = 0
        
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i]*l1[i]%l2[j]==0:
                    k = l1[i]*l1[i]//l2[j]
                    res += cnt[k]
                    
                    if l2[j]==k:
                        res -= 1
        
        return res//2
    
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.calc(nums1, nums2)+self.calc(nums2, nums1)
