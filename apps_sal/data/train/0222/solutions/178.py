class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexDict = {a: index for index, a in enumerate(A)}
        indexToLength = {}
        aLength = len(A)

        def computeMaxFibonacci(i, j):
            if (i, j) in indexToLength:
                return indexToLength[(i, j)]
            else:
                first = A[i]
                second = A[j]
                second += first
                first = second - first
                if second in indexDict:
                    answer = 1 + computeMaxFibonacci(j, indexDict[second])
                else:
                    answer = 2
                indexToLength[(i, j)] = answer
                return answer
        maxFib = 0
        for i in range(aLength):
            for j in range(i + 1, aLength):
                maxFib = max(maxFib, computeMaxFibonacci(i, j))
        return maxFib if maxFib >= 3 else 0
