class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        firstLessR = []
        firstLessL = []
        
        n = len(A)
        for i in range(n):
            firstLessR.append(i)
            firstLessL.append(i)
        
        incNums = []
        
        for i in range(n):
            if i == 0:
                incNums.append(i)
            else:
                while len(incNums) > 0 and A[incNums[-1]] >= A[i]:
                    firstLessR[incNums[-1]] = i
                    incNums.pop()
                incNums.append(i)
        
        for i in incNums:
            firstLessR[i] = n
        
        incNums = []
        for i in range(n-1, -1, -1):
            if i == n-1:
                incNums.append(i)
            else:
                while len(incNums) > 0 and A[incNums[-1]] > A[i]:
                    firstLessL[incNums[-1]] = i
                    incNums.pop()
                incNums.append(i)
        
        for i in incNums:
            firstLessL[i] = -1
        ans = 0
        #print(firstLessR, firstLessL)
        for i in range(n):
            w = (firstLessR[i] - i) * (i - firstLessL[i])
            ans += w * A[i]
            ans = ans % 1000000007
        
        return ans
