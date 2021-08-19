"""
https://leetcode.com/problems/get-the-maximum-score/


aproach 1: recursion brute force
  max(i+1, arr2[]) time O(n^n) space O(1)
 
approach 2: dp time O(n) space(n)


"""


class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dict1 = {}
        dict2 = {}
        for i in range(len(nums1)):
            dict1[nums1[i]] = i
        for i in range(len(nums2)):
            dict2[nums2[i]] = i
        dp1 = [0 for _ in nums1]
        dp2 = [0 for _ in nums2]

        def sol(index, curr):
            if curr == 1:
                if index == len(nums1):
                    return 0
                if not dp1[index]:
                    if nums1[index] in dict2:
                        indx2 = dict2[nums1[index]]
                        dp1[index] = max(sol(index + 1, curr), sol(indx2 + 1, 2)) + nums1[index]
                    else:
                        dp1[index] = sol(index + 1, curr) + nums1[index]
                return dp1[index]
            else:
                if index == len(nums2):
                    return 0
                if not dp2[index]:
                    if nums2[index] in dict1:
                        indx2 = dict1[nums2[index]]
                        dp2[index] = max(sol(index + 1, curr), sol(indx2 + 1, 1)) + nums2[index]
                    else:
                        dp2[index] = sol(index + 1, curr) + nums2[index]
                return dp2[index]
        sol(0, 1)
        sol(0, 2)
        return max(dp1[0], dp2[0]) % (10 ** 9 + 7)
