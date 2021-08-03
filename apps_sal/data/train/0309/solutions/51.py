class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}  # storing next Item -> (diff pattern, length so far)
        # [a, b, c]
        maxLength = 2

        if len(A) < 3:
            return len(A)

        for i in range(len(A)):  # iterating over A
            if A[i] in memo:
                toIter = [(i, j) for i, j in list(memo[A[i]].items())]
                del memo[A[i]]
                for k in toIter:
                    diff, length = k
                    if length > maxLength:
                        maxLength = length
                    length += 1

                    newKey = A[i] + diff
                    if newKey not in memo:
                        memo[newKey] = {}
                    if diff in memo[newKey]:
                        memo[newKey][diff] = max(length, memo[newKey][diff])
                    else:
                        memo[newKey][diff] = length
            for j in range(i):
                diff = A[i] - A[j]
                newKey = A[i] + diff
                if A[i] + diff not in memo:
                    memo[newKey] = {}
                if diff not in memo[newKey]:
                    memo[newKey][diff] = 3

        return maxLength
