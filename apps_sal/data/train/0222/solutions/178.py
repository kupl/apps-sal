class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexDict = {a:index for index,a in enumerate(A)}
        indexToLength = {}
        aLength = len(A)
        def computeMaxFibonacci(i,j):##gives the value of the longest sequence that starts with A[i] and A[j]. We assume that i < j. We are told it is strictly increasing so we are going to get monotonically decreasing sequences.
            if (i,j) in indexToLength:
                return indexToLength[(i,j)]
            else:
                first = A[i]
                second = A[j]
                second += first
                first = second-first
                if second in indexDict:
                    answer = 1+computeMaxFibonacci(j,indexDict[second])
                else:
                    answer = 2
                indexToLength[(i,j)] = answer
                return answer
        maxFib = 0   
        for i in range(aLength):
            for j in range(i+1,aLength):##we have to ensure that i < j.
                maxFib = max(maxFib,computeMaxFibonacci(i,j))
        ##print(indexToLength)
        return maxFib if maxFib >= 3 else 0##however it isn't as simple as returning maxFib because if it happens to be 2, then we need to return 0 per conditions of problem. Need to always consider test cases that would give variety of outputs.
        

