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
        if nonNeg:
            return temp
        
        res = float('-inf')
        
        rightWindow = [A[0]] + [0] * (len(A)-1)
        for idx,i in enumerate(A[1:]):
            rightWindow[idx+1] = i+rightWindow[idx]

            
        currMax = float('-inf')
        MaxIdx = float('inf')
        reversedA = A.reverse()
        leftWindow = [A[0]] + [0] * (len(A)-1)
        
        for idx,i in enumerate(A[1:]):
            leftWindow[idx +1] = i+leftWindow[idx]
            
            if MaxIdx >= len(A)-idx-1:
                currMax = max(rightWindow[:len(A)-idx-1])
                MaxIdx = rightWindow.index(currMax)

            res = max(res,currMax + leftWindow[idx])
        

        return max(res,temp)

