class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        def helper(nums):
            result = 0

            positiveSoFar = 0
            negativeSoFar = 0

            for i in range(len(nums)):
                if nums[i] == 0:
                    positiveSoFar = 0
                    negativeSoFar = 0
                elif nums[i] > 0 :
                    positiveSoFar += 1
                    if negativeSoFar > 0:
                        negativeSoFar += 1

                elif nums[i] < 0:
                    if negativeSoFar > 0:
                        positiveSoFar = max(negativeSoFar, positiveSoFar) +1
                        negativeSoFar = 0
                    else:
                        negativeSoFar = positiveSoFar + 1
                        positiveSoFar = 0

                result = max(result, positiveSoFar)
            return result
        
        # scan from left and scan from right
        return max(helper(nums), helper(nums[::-1]))
        

