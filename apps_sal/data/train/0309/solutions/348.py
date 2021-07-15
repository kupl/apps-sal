class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        
        dict = {}
        maxLength = 2
        for i in range(len(A) - 1):
            sameNumEncountered = False
            for j in range(i + 1, len(A)):
                dif = A[j] - A[i]
                
                if (i, dif) not in dict:
                    dict[j, dif] = 2
                else:
                    dict[j, dif] = dict[i, dif] + 1
                maxLength = max(maxLength, dict[j, dif])
                
        return maxLength

