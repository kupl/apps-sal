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
                if dif not in dict:
                    dict[dif] = {}
                if A[i] not in dict[dif]:
                    dict[dif][A[j]] = 2
                elif dif != 0 or not sameNumEncountered:
                    dict[dif][A[j]] = dict[dif][A[i]] + 1
                if dif == 0:
                    sameNumEncountered = True
                maxLength = max(maxLength, dict[dif][A[j]])
        return maxLength
