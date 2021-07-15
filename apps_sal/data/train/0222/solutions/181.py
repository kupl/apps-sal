from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        result = 0
        starterAtIdx = [] # starterAtIdx[i] = {numbers}, where each next num is A[i] + A[j] where j < i
        fullSeqAtIdx = [] # fullSeqAtIdx[i] = {num: length}, where num is next number in seq of length
        for idx, num in enumerate(A):
            starter = set()
            fullSeq = defaultdict(int)
            for j in range(0, idx):
                prevNum = A[j]
                if num in starterAtIdx[j]:
                    fullSeq[prevNum + num] = max(fullSeq[prevNum + num], 3)
                if num in fullSeqAtIdx[j]:
                    fullSeq[prevNum + num] = max(fullSeq[prevNum + num], 1 + fullSeqAtIdx[j][num])
                result = max(result, fullSeq[prevNum + num])
                starter.add(num + prevNum)
            starterAtIdx.append(starter)
            fullSeqAtIdx.append(fullSeq)
        return result
