class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A)
        wordLen = len(A[0])

        table = [1 for _ in range(wordLen)]

        for i in range(wordLen - 2, -1, -1):
            subAnsSet = set()
            for k in range(i + 1, wordLen):
                if A[0][i] <= A[0][k]:
                    subAnsSet.add(k)
            for j in range(1, N):
                nextSubAnsSet = set()
                for k in subAnsSet:
                    if A[j][i] <= A[j][k]:
                        nextSubAnsSet.add(k)
                subAnsSet &= nextSubAnsSet
            table[i] = max([table[k] + 1 for k in subAnsSet] + [1])
        return wordLen - max(table)
