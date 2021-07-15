from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        highest = 0
        offsets = [None] * len(A)
        for i in range(len(A)):
            offsets[i] = defaultdict(int)
        for i in range(len(A) - 1,-1,-1):
            # go forwards
            for j in range(i,-1,-1):
                offset = A[i] - A[j]
                if offset == 0:
                    continue
                offsets[i][offset] = 1
            # go backwards
            seen_offsets = set()
            for j in range(i,len(A)):
                offset = (A[i] - A[j]) * -1
                if offset == 0 or offset in seen_offsets:
                    continue
                seen_offsets.add(offset)
                # increment only for the first time we've seen this offset going back
                offsets[i][offset] += offsets[j][offset]
                if offsets[i][offset] > highest:
                    highest = offsets[i][offset]
        #for offset in offsets:
        #    print(offset)
        return highest + 1
