class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)
        sequenceEnds = dict()
        maxSequenceLen = 2
        for i in range(len(A)):
            seenDiffs = set()
            for j in range(i):
                diff = A[i] - A[j]
                if diff in seenDiffs:
                    continue
                elif diff in sequenceEnds:
                    sequencesWithDiff = sequenceEnds[diff]
                    if A[j] in sequencesWithDiff:
                        sequenceLength = sequencesWithDiff[A[j]]
                        sequencesWithDiff[A[i]] = sequenceLength + 1
                        maxSequenceLen = max(maxSequenceLen, sequenceLength + 1)
                    else:
                        sequencesWithDiff[A[i]] = 2
                else:
                    sequencesWithDiff = dict()
                    sequencesWithDiff[A[i]] = 2
                    sequenceEnds[diff] = sequencesWithDiff
                seenDiffs.add(diff)
        return maxSequenceLen
