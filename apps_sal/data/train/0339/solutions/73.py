import math


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = 0
        d = {}
        ans = 0
        for i in range(0, len(nums2)):
            for j in range(i + 1, len(nums2)):
                if(i != j):
                    p = (nums2[i] * nums2[j])
                    try:
                        d[p] += 1
                    except:
                        d[p] = 1
        for i in range(0, len(nums1)):
            p = nums1[i] * nums1[i]
            try:
                if(d[p] > 0):
                    cnt = cnt + d[p]
            except:
                ans = 1
        d = {}
        for i in range(0, len(nums1)):
            for j in range(i + 1, len(nums1)):
                if(i != j):
                    p = (nums1[i] * nums1[j])
                    try:
                        d[p] += 1
                    except:
                        d[p] = 1
        for i in range(0, len(nums2)):
            p = nums2[i] * nums2[i]
            try:
                if(d[p] > 0):
                    cnt = cnt + d[p]
            except:
                ans = 1
        return cnt
