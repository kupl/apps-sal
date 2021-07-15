class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # [idxnums1,idxnums2,value]
        changeSum = 0
        partialSums = [[0,0]]
        i,j,k=0,0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                changeSum = (changeSum + nums1[i]) % (10**9 + 7)
                i += 1
                j += 1
                partialSums.append([0,0])
            elif nums1[i] < nums2[j]:
                partialSums[-1][0] += nums1[i]
                i += 1
            else:
                partialSums[-1][1] += nums2[j]
                j += 1
        while i < len(nums1):
            partialSums[-1][0] += nums1[i]
            i += 1
        while j < len(nums2):
            partialSums[-1][1] += nums2[j]
            j += 1
            
        print(changeSum)
        print(partialSums)
        for i in partialSums:
            changeSum += max(i)
        return changeSum % (10**9 + 7)
                

