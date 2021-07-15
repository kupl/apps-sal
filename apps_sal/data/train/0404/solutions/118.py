class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if K == 1:
            return sum(A)/len(A)
        biggest = [[[None for temp in range(K+1)] for col in range(len(A))] for row in range(len(A))]
        for start in range(len(A)):
            for end in range(start,len(A),1):
                biggest[start][end][1] = sum(A[start:end+1])/len(A[start:end+1])
        for curK in range(2,K+1):
            startEnd = len(A)-curK+1
            if curK == K:
                startEnd = 1
            for start in range(0,startEnd,1):
                tempNo = 0
                for middle in range(start,len(A)-curK+1,1):
                    theNo = biggest[start][middle][1] + biggest[middle+1][len(A)-1][curK-1]
                    if theNo > tempNo:
                        tempNo = theNo
                biggest[start][len(A)-1][curK] = tempNo

            
        return (biggest[0][len(A)-1][K])

