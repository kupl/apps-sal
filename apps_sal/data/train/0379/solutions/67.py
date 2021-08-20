class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        index1 = 0
        index2 = 0
        score1 = 0
        score2 = 0
        maxScore = 0
        while index1 < l1 and index2 < l2:
            n1 = nums1[index1]
            n2 = nums2[index2]
            if n1 == n2:
                score1 += n1
                score2 += n2
                if score1 < score2:
                    maxScore += score2
                else:
                    maxScore += score1
                score1 = 0
                score2 = 0
                index1 += 1
                index2 += 1
            elif n1 < n2:
                score1 += n1
                index1 += 1
            else:
                score2 += n2
                index2 += 1
        for i in range(index1, l1):
            score1 += nums1[i]
        for i in range(index2, l2):
            score2 += nums2[i]
        if score1 < score2:
            maxScore += score2
        else:
            maxScore += score1
        return maxScore % (10 ** 9 + 7)
