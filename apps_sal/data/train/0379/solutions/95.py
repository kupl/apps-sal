'''
This seems to be dynamic programming where we have to find out the maximum score we can possibly get given the number of elements left to see in nums1 and nums2
'''
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        BIG_INT = 10**9+7
        maxSums = {}
        num1Values = {}
        num2Values = {}
        num1Values[0] = -1
        for index, num in enumerate(nums1):
            num1Values[num] = index
        num2Values[0] = -1
        for index,num in enumerate(nums2):
            num2Values[num] = index
        num1Length = len(nums1)
        num2Length = len(nums2)
        nums1.append(0)
        nums2.append(0)
        def computeMaxSum(num1Left,num2Left):
            ##print(\"(num1Left,num2Left) is: \"+str((num1Left,num2Left)))
            if num1Left*num2Left == 0:
                return 0
            else:
                if (num1Left,num2Left) in maxSums:
                    return maxSums[(num1Left,num2Left)]
                current1 = 0 if num1Left == num1Length+1 else nums1[-num1Left-1]##had to do -num1Left-1 because we append 0 for future purposes of termination.
                current2 = 0 if num2Left == num2Length+1 else nums2[-num2Left-1]
                ##print(\"(current1,current2) is: \"+str((current1,current2)))
                if current1 == current2:
                    maxSums[(num1Left,num2Left)] = max(computeMaxSum(num1Left-1,num2Left)+nums1[-num1Left], computeMaxSum(num1Left,num2Left-1)+nums2[-num2Left])
                elif current1 > current2:
                    ##we can either progress to the next in current1 or possibly swap to current2.
                    if current1 in num2Values:
                        new2Index = num2Values[current1]
                        maxSums[(num1Left,num2Left)] = computeMaxSum(num1Left,num2Length-new2Index)##remember you do computeMaxSum before actually calling dictionary because you haven't set it in dictionary yet.
                    else:
                        maxSums[(num1Left,num2Left)] = computeMaxSum(num1Left-1,num2Left)+nums1[-num1Left]
                else:
                    ##we can either progress to the next in current2 or possibly swap to current1.
                    if current2 in num1Values:
                        new1Index = num1Values[current2]
                        maxSums[(num1Left,num2Left)] = computeMaxSum(num1Length-new1Index,num2Left)
                    else:
                        maxSums[(num1Left,num2Left)] = computeMaxSum(num1Left,num2Left-1)+nums2[-num2Left]
                return maxSums[(num1Left,num2Left)]
        return computeMaxSum(num1Length+1,num2Length+1)%BIG_INT

