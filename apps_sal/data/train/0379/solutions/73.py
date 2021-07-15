# 1537. Get the Maximum Score

from math import inf

def mix (A, B):
    ans = []
    i, j = 0, 0
    while i < len (A) or j < len (B):
        if i == len (A):   choice = 2
        elif j == len (B): choice = 1
        elif A[i] < B[j]:  choice = 1
        elif A[i] > B[j]:  choice = 2
        else:              choice = 3

        if choice == 1:
            ans.append ((A[i], choice))
            i += 1
        elif choice == 2:
            ans.append ((B[j], choice))
            j += 1
        elif choice == 3:
            ans.append ((A[i], choice))
            i, j = i+1, j+1
    return ans

def find_max (C, init):
    max0, max1 = -inf, -inf
    for i, (val, branches) in enumerate (C):
        if val == init:
            if branches == 1:
                new0, new1 = val, -inf
            elif branches == 2:
                new0, new1 = -inf, val
            else:
                new0, new1 = val, val
        else:
            if branches == 1:
                new0, new1 = max0 + val, max1
            elif branches == 2:
                new0, new1 = max0, max1 + val
            elif branches == 3:
                new0, new1 = max (max0, max1) + val, max (max0, max1) + val
        max0, max1 = new0, new1
    return max (max0, max1)

def find_max_score (A, B):
    C = mix (A, B)
    return max (find_max (C, A[0]), find_max (C, B[0]))

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        return find_max_score(nums1, nums2) % (10**9 + 7)
