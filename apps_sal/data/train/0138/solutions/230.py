class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        def helper(nums):
            result = 1 if nums[0] > 0 else 0

            positiveSoFar = 1 if nums[0] > 0 else 0
            negativeSoFar = 1 if nums[0] < 0 else 0


            for i in range(1, len(nums)):
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
        
        
        return max(helper(nums), helper(nums[::-1]))
        

