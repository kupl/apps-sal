class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        def maxSubarray (A):
            dp = [0] * len(A)
            max_c = A[0]
            flag = True
            for idx,num in enumerate(A):
                if num < 0:
                    flag = False
                if idx == 0:
                    dp[0]=num
                else:
                    dp[idx]=max(num, dp[idx-1] + num)
            return max(dp), flag
        
        temp,nonNeg = maxSubarray(A)

        
        res = float('-inf')
        rightMax = [max(A[0],0)] + [0] * (len(A)-1)
        currMax = max(A[0],0)
        rightWindow = [A[0]] + [0] * (len(A)-1)
        for idx,i in enumerate(A[1:]):
            currMax = max(i+rightWindow[idx], currMax)
            rightMax[idx+1] = currMax
            rightWindow[idx+1] = i+rightWindow[idx]
        

        reversedA = A.reverse()
        leftWindow = [A[0]] + [0] * (len(A)-1)
        
        for idx,i in enumerate(A[1:]):
            leftWindow[idx +1] = i+leftWindow[idx]
            currMax = rightMax[len(A)-idx-2]
            res = max(res,currMax + leftWindow[idx])
        

        return max(res,temp)

